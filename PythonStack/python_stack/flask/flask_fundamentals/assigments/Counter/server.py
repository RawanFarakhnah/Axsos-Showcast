from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def index():
    if "counter" not in session: 
       session['counter'] = 0
    else:
        session['counter'] += 1
    return render_template("index.html")

@app.route('/increase', methods=['POST'])
def increase():
    session['counter'] = session.get('counter', 0) + 2
    return redirect(url_for('index'))

@app.route('/custom_increase', methods=['POST'])
def custom_increase():
    custom_counter = request.form['custom_counter']
    session['counter'] = session.get('counter', 0) + int(custom_counter)
    return redirect(url_for('index'))

@app.route('/destroy_session', methods=['POST'])
def clear_session():
    session.clear()
    return redirect(url_for('index'))
    
if __name__ == "__main__":
    app.run(debug=True)
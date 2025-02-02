from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = '8f895499bf8b4deb9ff54e4743ea0411'

@app.route('/')
def home():
    return render_template('form.html')

# @app.route('/add-user', methods=['POST'])
# def register():
#     data = request.form
#     if 'counter' not in session:
#         session['counter'] = 0
#     session['counter'] += 1
#     return render_template('success.html', data=data, counter=session['counter'])

@app.route('/add-user', methods=['POST'])
def register():
    data = request.form
    print("MY_Data" , data)
    return redirect('/success') #this solve re-submitted request 

@app.route('/success')
def show_user():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)
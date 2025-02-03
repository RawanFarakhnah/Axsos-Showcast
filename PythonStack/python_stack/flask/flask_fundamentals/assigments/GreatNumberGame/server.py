from flask import Flask, render_template, redirect, url_for, session, request
from  random import randrange

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def index():
    if 'random' not in session:
        session['random'] = randrange(1, 101)

    if 'attempts' not in session:
        session['attempts'] = 0
    
    print("session['random']", session['random'])
    return render_template('index.html',success=False, message = "")

@app.route('/try_again')
def try_again():
    session.clear()
    return redirect(url_for('index'))

@app.route('/guess_number', methods=['POST'])
def guess_number():
    guess = int(request.form['guess_number'])
    session['attempts'] += 1

    if guess == session['random']:
        return render_template('index.html', success=True)
    elif guess < session['random']:
        return render_template('index.html', success=False, message= "Too Low!")
    else:
        return render_template('index.html', success=False, message = "Too High!")

if __name__ == "__main__":
    app.run(debug=True)
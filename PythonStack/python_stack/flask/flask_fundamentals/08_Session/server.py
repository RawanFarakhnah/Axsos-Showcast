from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "your_key_Id"

@app.route('/')
def home():
    return render_template("form.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['fullName']
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    name_on_template=session['username'],
    email_on_template=session['useremail']
    return render_template('show.html')

if __name__ == "__main__":
    app.run(debug=True)


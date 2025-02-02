from flask import Flask,render_template

app = Flask(__name__)

#Handling Root Route
@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times= 5)


if __name__ == "__main__":
    app.run(debug=True)
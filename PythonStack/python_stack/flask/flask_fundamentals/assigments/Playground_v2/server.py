from flask import Flask, render_template

app = Flask(__name__)
default_color = "rgb(159, 197, 248)"

@app.route('/')
def index():
    return "<h1>Welcome to Playground</h1>"

@app.route('/play')
def play_default_boxes():
    return render_template("index.html", boxes=3, color=default_color)

@app.route('/play/<int:x>')
def play_x_boxes(x):
    return render_template("index.html", boxes=x, color=default_color)

@app.route('/play/<int:x>/<color>')
def play_x_color_boxes(x,color):
    return render_template("index.html", boxes=x, color=color)

if __name__ == "__main__":
    app.run(debug=True)
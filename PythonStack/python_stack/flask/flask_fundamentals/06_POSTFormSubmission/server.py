from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get-register')
def show_get_form():
    return render_template("form_with_get.html")

@app.route('/add_with_get', methods=['GET'])
def add_with_get_form():
   data = request.args # Use `request.args` for GET requests
   return render_template("success.html",data=data)

@app.route('/post-register')
def show_post_form():
    return render_template("form_with_post.html")

@app.route('/add_with_post', methods=['POST'])
def add_with_post_form():
   data = request.form
   return render_template("success.html",data=data)

if __name__ == "__main__":
    app.run(debug=True)
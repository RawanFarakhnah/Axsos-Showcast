from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/Champion')
def say_champion():
    return "Champion!"


@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:times>/<message>')
def say_repeatedly_something(times, message):
    output = ""
    for i in range(times):
        output += f"{message} \n"
    return output
    
@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)
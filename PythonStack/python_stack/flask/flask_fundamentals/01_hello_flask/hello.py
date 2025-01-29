#act as server file
#we will set up all routes to handle requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
   app.run(debug=True)
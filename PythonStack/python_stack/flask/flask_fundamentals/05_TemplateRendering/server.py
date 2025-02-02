from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/lists')
def render_lists():
    student_info = [
           {'name' : 'Michael', 'age' : 35},
           {'name' : 'John', 'age' : 30 },
           {'name' : 'Mark', 'age' : 25},
           {'name' : 'KB', 'age' : 27}
        ]
    
    return render_template("index.html",
                           random_numbers= [3,1,5],
                           student_info =student_info
                           )

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", 
                           rows=8,
                           colms=8,
                           color1="black",
                           color2="red"
                           )

@app.route('/<int:rows>')
def index_row (rows):
    return render_template("index.html", 
                           rows=rows,
                           colms=8,
                           color1="black",
                           color2="red"
                           )

@app.route('/<int:rows>/<int:colms>')
def index_row_colms (rows,colms):
    return render_template("index.html", 
                           rows=rows,
                           colms=colms,
                           color1="black",
                           color2="red"
                           )

@app.route('/<int:rows>/<int:colms>/<color1>/<color2>')
def index_flexible (rows,colms,color1,color2):
    return render_template("index.html", 
                           rows=rows,
                           colms=colms,
                           color1=color1,
                           color2=color2
                           )

if __name__ == "__main__":
    app.run(debug=True)
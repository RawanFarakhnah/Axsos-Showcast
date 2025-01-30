from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/result", methods=['POST'])
def viewResult():
   formOutput = request.form
   selected_communications = request.form.getlist("communication")
   selected_satisfaction = request.form.getlist("satisfaction")
    
   return render_template("view.html",formOutput=formOutput, selected_communications = selected_communications,selected_satisfaction=selected_satisfaction)
  
if __name__ == "__main__":
  app.run(debug=True)
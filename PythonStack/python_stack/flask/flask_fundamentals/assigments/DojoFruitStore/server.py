from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    # print(request.form) #FOR DEBUG
    formOutput = request.form
    count = int(formOutput['apple']) + int(formOutput['strawberry']) + int(formOutput['raspberry'])    
    return render_template("checkout.html", formOutput=formOutput,count=count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
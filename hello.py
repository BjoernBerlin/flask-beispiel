from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

email_adresses = []

@app.route("/")
def hello():
    return render_template('index.html')
                                                                 
@app.route("/signup", methods = ['POST'])
def signup():
    email = request.form['email']
    email_adresses.append(email)
    print(email_adresses)
    return redirect('/')    
    
if __name__ == "__main__":
    app.run(debug=True)

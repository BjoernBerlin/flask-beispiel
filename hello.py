from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')
                                                                 
@app.route("/signup", methods = ['POST'])
def signup():
    email = request.form['email']
    print("Ihre Email-Adresse ist '" + email +"'")
    return redirect('/')    
    
if __name__ == "__main__":
    app.run(debug=True)

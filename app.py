from flask import Flask
from flask import Flask, render_template
from flask import Flask, render_template, json, request


app = Flask(__name__)
@app.route("/")
@app.route('/showSignUp')
@app.route('/signUp',methods=['POST'])

def showSignUp():
   return render_template('signup.html')

def main():
     return render_template('index.html')
    
if __name__ == "__main__":
    app.run()
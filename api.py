from flask import Flask, render_template
#import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/questions.html')
def question():
    return render_template("questions.html")

@app.route("/display.html")
def display():
    return render_template("display.html")

if __name__ == '__main__':
    app.run(debug=True)
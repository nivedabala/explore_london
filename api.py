from flask import Flask, render_template
import csv

app = Flask(__name__)

#@app.route('/', methods=['GET'])
#def api():
    #return {
        #'userId':1,
        #'title': 'Flask React Application',
        #'completed': False
    #}
@app.route('/')
def home():
    return render_template("home.html")

@app.route("/question")
def question():
    return render_template("questions.html")

@app.route("/display")
def display():
    return render_template("display.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
<<<<<<< HEAD
from flask import Flask, render_template
#import csv

app = Flask(__name__)

=======
from flask import Flask, request, render_template, redirect, url_for
import csv

app = Flask(__name__)


# @app.route('/', methods=['GET'])
# def api():
# return {
# 'userId':1,
# 'title': 'Flask React Application',
# 'completed': False
# }
>>>>>>> 74c333c638a201f7e96fb14bc7e71585de165598
@app.route('/')
def home():
    return render_template("home.html")

<<<<<<< HEAD
@app.route('/questions.html')
def question():
    return render_template("questions.html")

@app.route("/display.html")
=======

@app.route("/questions", methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        return redirect(url_for('home'))

    return render_template('questions.html')


@app.route("/display", methods=['GET', 'POST'])
>>>>>>> 74c333c638a201f7e96fb14bc7e71585de165598
def display():
    if request.method == 'POST':
        return redirect(url_for('home'))

    return render_template('display.html')


if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(debug=False, host='localhost',port=5001)
>>>>>>> 74c333c638a201f7e96fb14bc7e71585de165598

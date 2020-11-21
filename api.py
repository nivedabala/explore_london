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
@app.route('/')
def home():
    return render_template("home.html")


@app.route("/questions", methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        return redirect(url_for('home'))

    return render_template('questions.html')


@app.route("/display", methods=['GET', 'POST'])
def display():
    if request.method == 'POST':
        return redirect(url_for('home'))

    return render_template('display.html')


if __name__ == '__main__':
    app.run(debug=False, host='localhost')

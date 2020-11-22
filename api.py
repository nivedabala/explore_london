from flask import Flask, request, render_template, redirect, url_for
import csv
import os

PICTURE_FOLDER = os.path.join('static', 'picture_photo')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PICTURE_FOLDER

#from pathplanner import Session

# @app.route('/', methods=['GET'])
# def api():
# return {
# 'userId':1,
# 'title': 'Flask React Application',
# 'completed': False
# }
@app.route('/')
def home():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'explore.png')
    return render_template("home.html", user_image = full_filename)


@app.route("/questions", methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        return redirect(url_for('home'))

    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'explore.png')
    return render_template('questions.html', user_image = full_filename)


@app.route("/index", methods=['GET', 'POST'])
def index():
    locations = []
    if request.method == 'GET':
        locations = ["54 clifford fairbarn dr, ONT", "36 peter miller st, ONT"]


    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'download.png')
    return render_template('index.html', user_image = full_filename, locations=locations)


if __name__ == '__main__':
    app.run(debug=True, host='localhost',port=5001)

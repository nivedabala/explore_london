from flask import Flask, render_template, request
app = Flask(name)
@app.route('/')
def questions():
   return render_template('questions.html')


@app.route('/display',methods = ['POST', 'GET'])
def display():
   if display.method == 'POST':
      display = display.form
      return render_template("display.html",display = display)


if name == 'main':
   app.run(debug = True)
import json
import requests
from bs4 import BeautifulSoup
import datetime
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
    greeding = "Hello World"
    return greeding

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
   if request.method == 'POST':
        dates = request.form['h']
        data = datetime.datetime(dates)

        homeUrl = '/form'
        return render_template("confirm.html", data=data, homeUrl=homeUrl)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
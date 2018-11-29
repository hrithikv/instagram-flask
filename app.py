import json
import requests
from bs4 import BeautifulSoup
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
        username = request.form['username']
        url = 'https://www.instagram.com/{0}/'.format(username)
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'lxml')
        entryDict = json.loads(str(soup.select_one('body > script:nth-of-type(1)').text).split('=', 1)[1][1:-1])
        data = entryDict['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
        homeUrl = '/form'
        return render_template("confirm.html", data=data, homeUrl=homeUrl)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
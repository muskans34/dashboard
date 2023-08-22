import secrets

import pymongo
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['test']
collection = db['assesment']


@app.route('/')
def dash():
    data = list(collection.find({}, {"_id": '64cd1a1925c700eabb980a98'}))
    return render_template('dash.html', data=data)


@app.route('/data')
def data():
    return render_template('')


@app.route("/chart")
def chart():
    return render_template("chart.html")


if __name__ == '__main__':
    app.run(debug=True)

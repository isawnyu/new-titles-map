import os

from flask import Flask, render_template, url_for, jsonify
from sqlalchemy import extract
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import NewTitles


@app.route('/')
def index():
    cols = ['bsn', 'latitude', 'longitude']
    data = NewTitles.query.all()
    result = [{col: str(getattr(d, col)) for col in cols} for d in data]
    return render_template('index.html', result=result)

@app.route('/<year>')
def titles_by_year(year):
    cols = ['bsn', 'latitude', 'longitude', 'date']
    data = NewTitles.query.filter(extract('year', NewTitles.date) == year).all()
    result = [{col: str(getattr(d, col)) for col in cols} for d in data]
    return render_template('index.html', result=result)


@app.route('/<year>/<month>')
def titles_by_month(year, month):
    cols = ['bsn', 'latitude', 'longitude', 'date']
    data = NewTitles.query.filter(extract('year', NewTitles.date) == year).filter(extract('month', NewTitles.date) == month).all()
    result = [{col: str(getattr(d, col)) for col in cols} for d in data]
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run()

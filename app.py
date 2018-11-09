import os

import calendar

from flask import Flask, render_template, url_for, jsonify, redirect
from sqlalchemy import extract
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import NewTitles

def _get_max_date(model):
    dates = model.query.order_by(model.date.desc()).limit(1).one()
    return dates.date

def _get_highest_year(date):
    NewTitles.query.order_by('updated desc').limit(1)
    years = NewTitles.query.filter(extract('year', NewTitles.date) == year).all()
    return max(years)

def _get_highest_month():
    data = NewTitles.query.filter(extract('year', NewTitles.date) == year).filter(extract('month', NewTitles.date) == month).all()


def _get_rel_date(date, offset):
    return date + relativedelta(months=offset)


@app.route('/')
def index():
    max_date = _get_max_date(NewTitles)
    return redirect(url_for('titles_by_month',
        year=max_date.year,
        month=max_date.month,),
            code=307)

@app.route('/all')
def titles_all():
    cols = ['bsn', 'latitude', 'longitude']
    data = NewTitles.query.all()
    result = [{col: str(getattr(d, col)) for col in cols} for d in data]
    return render_template('index.html', result=result, period=None)

@app.route('/<year>')
def titles_by_year(year):
    cols = ['bsn', 'latitude', 'longitude', 'date']
    data = NewTitles.query.filter(extract('year', NewTitles.date) == year).all()
    result = [{col: str(getattr(d, col)) for col in cols} for d in data]
    return render_template('index.html', result=result, period=year)


@app.route('/<year>/<month>')
def titles_by_month(year, month):

    date = datetime(year=int(year), month=int(month), day=1)
    prev_date = _get_rel_date(date, -1)
    next_date = _get_rel_date(date, 1)

    cols = ['bsn', 'latitude', 'longitude', 'date']
    data = NewTitles.query.filter(extract('year', NewTitles.date) == year).filter(extract('month', NewTitles.date) == month).all()
    result = [{col: str(getattr(d, col)) for col in cols} for d in data]
    return render_template('index.html', result=result, period='{} {}'.format(calendar.month_name[int(month)], year), prev_year=prev_date.year, prev_month=prev_date.month, next_year=next_date.year, next_month=next_date.month)


if __name__ == '__main__':
    app.run()

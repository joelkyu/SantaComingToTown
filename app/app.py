from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from config import app
from models import db, Person, Characteristic
import os


@app.route('/')
def index():
    db.create_all()  # Initiate all objects
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add_person():
    lp = request.form['Lower-Price']
    hp = request.form['Upper-Price']
    if hp < lp:
        lp, hp = hp, lp  # switch variables if user inputs wrong price bracket.
    p = Person(twitter=request.form['Twitter-Handle'], lower_price=lp, upper_price=hp)
    db.session.add(p)
    db.session.commit()
    print(request.form)
    return render_template('index.html', people=Person.query.all())


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

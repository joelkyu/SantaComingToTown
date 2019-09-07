from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import app
from models import db, Person, Characteristic


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

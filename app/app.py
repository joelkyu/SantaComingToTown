from flask import Flask, render_template, request, url_for, jsonify
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
    lp = request.header['Lower-Price']
    hp = request.header['Upper-Price']
    if hp < lp:
        lp, hp = hp, lp  # switch variables if user inputs wrong price bracket.
    p = Person(twitter=request.header['Twitter-Handle'], lower_price=lp, upper_price=hp)
    db.session.add(p)
    db.session.commit()
    return jsonify(Person.query.all())


@app.route('/person/<int:person_id>', methods=['GET'])
def get_person(person_id):
    return jsonify(Person.query.get(person_id))


@app.route('/compare/<int:person_id>', methods=['GET'])
def get_comparison(person_id):
    description = request.header['name']
    price = request.header['price']
    compatible = {}
    for person in Person.query.all():
        c = person.compatibility(description, price)
        if c > 0:
            compatible[person.twitter] = c
    return jsonify(compatible)

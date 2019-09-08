from flask import Flask, render_template, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import app
from models import db, Person, Characteristic
import os


@app.route('/')
def index():
    db.create_all()
    db.session.add(Person(twitter="Alan", lower_price=5, upper_price=10))
    db.session.commit()
    return jsonify([p.deserialize() for p in Person.query.all()])  # Initiate all objects



@app.route('/add', methods=['POST'])
def add_person():
    db.create_all()
    lp = float(request.headers['Lower-Price'])
    hp = float(request.headers['Upper-Price'])
    if hp < lp:
        lp, hp = hp, lp  # switch variables if user inputs wrong price bracket.
    p = Person(twitter=request.headers['Twitter-Handle'], lower_price=lp, upper_price=hp)
    db.session.add(p)
    db.session.commit()
    return jsonify([p.deserialize() for p in Person.query.all()])


@app.route('/person/<int:person_id>', methods=['GET'])
def get_person(person_id):
    return jsonify(Person.query.get(person_id).deserialize())


@app.route('/compare/<int:person_id>', methods=['GET'])
def get_comparison(person_id):
    description = request.headers['name']
    price = request.headers['price']
    compatible = {}
    for person in Person.query.all():
        c = person.compatibility(description, price)
        if c > 0:
            compatible[person.twitter] = c
    return jsonify(compatible)


@app.route('/delete/<int:person_id>', methods=['POST'])
def delete_target(person_id):
    db.session.delete(Person.query.get(person_id))
    db.session.commit()
    return jsonify([p.deserialize() for p in Person.query.all()])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

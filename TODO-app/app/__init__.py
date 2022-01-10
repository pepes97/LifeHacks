


"""Setup at app startup"""
from flask import render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Text)
    status = db.Column(db.Text, default='Todo')

    def __init__(self, task):
        self.task = task
        self.status = 'Todo'

    def __repr__(self):
        return '<Task %s>' % self.task

db.create_all()

# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
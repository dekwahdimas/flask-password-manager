from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class PassManager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(150))
    platform = db.Column(db.String(150))
    add_email = db.Column(db.String(150))
    add_pass = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    pass_manager = db.relationship('PassManager')
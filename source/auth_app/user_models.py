from flask import abort
from flask_login import UserMixin, current_user
from sqlalchemy import func
from werkzeug.security import generate_password_hash, check_password_hash

from source.extensions import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    todos = db.relationship('ToDo', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
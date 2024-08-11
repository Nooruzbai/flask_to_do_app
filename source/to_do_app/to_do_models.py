from sqlalchemy import func, Enum

from source.extensions import db


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    due_date = db.Column(db.DateTime)
    priority = db.Column(Enum('low', 'medium', 'high', name='priority_levels'), nullable=False, default='low')
    status = db.Column(Enum('pending', 'in_progress', 'completed', 'archived', name='status_levels'), nullable=False,
                       default='pending')
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


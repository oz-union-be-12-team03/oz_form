from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    sqe = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 관계 설정
    image = db.relationship('Image', backref=db.backref('questions', lazy=True))
    choices = db.relationship('Choice', backref='question', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Question {self.id} - {self.title[:20]}>"

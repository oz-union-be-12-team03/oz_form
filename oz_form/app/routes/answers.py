from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #3팀 화이팅

class Answer(db.Model):
    __tablename__ ='answers'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    choice_id = db.Column(db.Integer, db.ForeignKey('choices.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    user = db.relationship('User', back_populates='answers')
    choice = db.relationship('Choice', back_populates='answers')
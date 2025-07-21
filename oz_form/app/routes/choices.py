from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, request, jsonify

db = SQLAlchemy()



    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    sqe = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    question = db.relationship('Question', back_populates='choices')
    answers = db.relationship('Answer', back_populates='choice')

# 블루프린트 생성
choices_blp = Blueprint('choices', __name__, url_prefix='/choices')

# POST: 선택지 생성
@choices_blp.route('/', methods=['POST'])
def create_choice():
    data = request.get_json()
    try:
        new_choice = Choice(
            question_id=data['question_id'],
            content=data['content'],
            sqe=data['sqe'],
            is_active=data.get('is_active', True)
        )
        db.session.add(new_choice)
        db.session.commit()
        return jsonify({"message": "Choice created", "choice_id": new_choice.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# GET: 특정 질문에 대한 선택지 리스트 조회
@choices_blp.route('/question/<int:question_id>', methods=['GET'])
def get_choices_by_question(question_id):
    choices = Choice.query.filter_by(question_id=question_id).all()
    return jsonify([
        {
            "id": c.id,
            "content": c.content,
            "sqe": c.sqe,
            "is_active": c.is_active
        } for c in choices
    ]), 200

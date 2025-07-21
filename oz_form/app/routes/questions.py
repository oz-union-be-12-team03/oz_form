from flask import jsonify, request, Blueprint
from app.models import Question, Image
from config import db
from datetime import datetime

questions_blp = Blueprint("questions", __name__)

# 질문 전체 조회
@questions_blp.route("/questions", methods=["GET"])
def get_all_questions():
    questions = Question.query.order_by(Question.sqe).all()
    result = []

    for q in questions:
        result.append({
            "id": q.id,
            "title": q.title,
            "image_url": q.image.url if q.image else None,
            "sqe": q.sqe,
            "is_active": q.is_active,
            "created_at": q.created_at.isoformat(),
            "updated_at": q.updated_at.isoformat(),
        })

    return jsonify({"questions": result}), 200

# 단일 질문 조회
@questions_blp.route("/question/<int:question_id>", methods=["GET"])
def get_question_by_id(question_id):
    question = Question.query.get(question_id)
    if not question:
        return jsonify({"message": "질문을 찾을 수 없습니다."}), 404

    return jsonify({
        "id": question.id,
        "title": question.title,
        "image_url": question.image.url if question.image else None,
        "sqe": question.sqe,
        "is_active": question.is_active,
        "created_at": question.created_at.isoformat(),
        "updated_at": question.updated_at.isoformat()
    }), 200
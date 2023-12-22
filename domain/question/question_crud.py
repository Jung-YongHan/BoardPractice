from datetime import datetime

from sqlalchemy.orm import Session

from domain.question.question_schema import QuestionCreate
from models import Question


def get_question_list(db: Session):
    question_list = db.query(Question)\
        .order_by(Question.create_date.desc())\
        .all()
    return question_list

def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question

def create_question(db: Session, question_create: QuestionCreate):
    db_question = Question(title=question_create.title,
                           content=question_create.content,
                           create_date=datetime.now())
    db.add(db_question)
    db.commit()
from datetime import datetime

from domain.question.question_schema import QuestionCreate
from models import Question


def get_question_list():
    question_list = Question.objects.order_by('-create_date')
    return question_list

def get_question(question_id: str):
    question = Question.objects(_id=question_id).first()
    return question

def create_question(question_create: QuestionCreate):

    new_question = Question(
        subject=question_create.subject,
        content=question_create.content,
        create_date=datetime.now()
    )
    new_question.save()
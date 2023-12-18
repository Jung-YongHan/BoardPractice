from datetime import datetime

from domain.answer.answer_schema import AnswerCreate
from models import Question, Answer

def create_answer(question: Question, answer_create: AnswerCreate):
    new_answer = Answer(
        content=answer_create.content,
        create_date=datetime.now()
    )
    question.answers.append(new_answer)
    question.save()
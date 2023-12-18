import datetime

from pydantic import BaseModel, Field, field_validator
from domain.answer.answer_schema import Answer

class QuestionCreate(BaseModel):
    subject: str
    content: str

    @field_validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

class Question(BaseModel):
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []

    class Config:
        populate_by_name = True
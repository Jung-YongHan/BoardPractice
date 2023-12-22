import datetime

# pydantic이란? FastAPI의 입출력 스펙을 정의하고 그 값을 검증하기 위해 사용하는 라이브러리
from pydantic import BaseModel, field_validator
from domain.answer.answer_schema import Answer

class QuestionCreate(BaseModel):
    title: str
    content: str

    @field_validator('title', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

class Question(BaseModel):
    id: int
    title: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []
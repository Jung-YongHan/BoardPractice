from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from domain.question import question_schema, question_crud
from database import get_db
from models import Question

router = APIRouter(
    prefix="/api/question",
)

# Depends는 매개변수로 전달 받은 함수를 실행시킨 결과를 리턴
# db객체에 get_db 제너레이터에 의해 생성된 세션 객체가 주입 됨.
# question_list 함수의 리턴값은 Question 스키마로 구성된 리스트임을 의미
@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    return _question_list

@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db)):
    question_crud.create_question(db=db, question_create=_question_create)
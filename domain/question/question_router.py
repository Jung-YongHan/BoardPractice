from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from domain.question import question_schema, question_crud


router = APIRouter(
    prefix="/api/question",
)


@router.get("/list", response_model=list[question_schema.Question])
def question_list():
    _question_list = question_crud.get_question_list()
    return _question_list

@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: str):
    question = question_crud.get_question(question_id=question_id)
    return question

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate):
    try:
        question_crud.create_question(question_create=_question_create)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

from bson import ObjectId
from fastapi import APIRouter, HTTPException
from starlette import status

from domain.answer import answer_schema, answer_crud
from domain.question import question_crud

router = APIRouter(
    prefix="/api/answer",
)


@router.post("/create/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def answer_create(question_id: str, _answer_create: answer_schema.AnswerCreate):

    # create answer
    question = question_crud.get_question(question_id=question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    answer_crud.create_answer(question=question, answer_create=_answer_create)

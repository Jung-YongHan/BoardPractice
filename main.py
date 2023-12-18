from mongoengine import connect
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from domain.answer import answer_router
from domain.question import question_router

app = FastAPI()

origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 설정
app.include_router(question_router.router)
app.include_router(answer_router.router)

# Connect to MongoDB
connect("myapi", host="localhost", port=27017)
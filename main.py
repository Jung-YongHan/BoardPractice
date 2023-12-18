from mongoengine import connect
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Server.repository.PostRepository import PostRepository
from motor.motor_asyncio import AsyncIOMotorClient
from Server.entity.PostModel import PostModel

from domain.answer import answer_router
from domain.question import question_router

from Server.Controller.MemberRouter import router as member_router

app = FastAPI()

origins = [
    "http://localhost:8080"
]

app.include_router(member_router)

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


"""
@app.get("/hello")
async def read_root():
    return {"Hello": "World"}

#http://127.0.0.1:8000/item/4?dsf=242
@app.get("/item/{item_id}")
async def read_item(item_id: int, dsf: str):
    return {"item_id": item_id, "dsf": dsf}



@app.get("/")
async def read_root():
    # MongoDB 컬렉션에서 비동기식으로 데이터를 읽는 예시
    some_collection = db.posts  # "some_collection"은 컬렉션 이름입니다.
    post = PostModel(_id=1, title="my", author="name", content="content here")

    await db.posts.insert_one(post.dict(by_alias=True))
    item = await some_collection.find_one()  # 첫 번째 문서를 비동기식으로 찾습니다.
    return {"Hello": "World", "item": item}
    """
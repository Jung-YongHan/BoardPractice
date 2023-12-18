import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from repository.PostRepository import PostRepository
from motor.motor_asyncio import AsyncIOMotorClient
from entity.PostModel import PostModel


from fastapi import FastAPI
from Controller.MemberRouter import router as member_router

app = FastAPI()

app.include_router(member_router)

app = FastAPI()

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.Board  # 여기서 "mydatabase"는 사용할 데이터베이스 이름입니다.


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)



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
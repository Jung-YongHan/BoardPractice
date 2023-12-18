import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from motor.motor_asyncio import AsyncIOMotorClient
from entity import PostModel


DB_URL="mongodb://localhost:27017"

client = AsyncIOMotorClient(DB_URL)
db = client.Board  # 'mydatabase'를 원하는 데이터베이스 이름으로 변경



class PostRepository:
    #삽입
    async def save_post(self,post: PostModel):
        await db.posts.insert_one(post.model_dump())
    
    #삭제
    async def delete_post(self,id: int):
        await db.posts.delete_one({"id":id})

    #수정 
    async def update_post(self,post_id: int, updated_data: dict):
        await db.posts.update_one({"id": post_id}, {"$set": updated_data})

    
    #검색
    async def search_posts(self,name: str):
        cursor = db.posts.find({"name": name})
        posts = await cursor.to_list(length=100)
        return posts




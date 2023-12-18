from motor.motor_asyncio import AsyncIOMotorClient
from Server.entity import PostModel
from datetime import datetime




DB_URL="mongodb://localhost:27017"

client = AsyncIOMotorClient(DB_URL)
db = client.Board  #Board는 원하는 db이름



class MemberRepository:
    #삽입
    async def save_member(self,post: PostModel):
        await db.members.insert_one(post.model_dump())
    
    #삭제
    async def delete_member(self,id: int):
        await db.members.delete_one({"id":id})

    #수정 
    async def update_member(self,post_id: int, updated_data: dict):
        await db.members.update_one({"id": post_id}, {"$set": updated_data})

    
    #검색
    async def search_members(self,id: str):
        cursor = db.members.find({"id": id})
        posts = await cursor.to_list(length=100)
        return posts

    async def search_member_by_id(self,id: str):
        return db.members.find_one({"id":id})
        
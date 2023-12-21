from motor.motor_asyncio import AsyncIOMotorClient
from member_schema import member_model





DB_URL="mongodb://localhost:27017"

client = AsyncIOMotorClient(DB_URL)
db = client.Board  #Board는 원하는 db이름



class MemberRepository:
    #삽입
    async def save_member(self,member: member_model):
    # _id 필드를 사용자 정의 아이디로 설정
        member_data = member.dict(by_alias=True)
        new_member = await db.members.insert_one(member_data)

        return {"status": "success", "member_id": str(new_member.inserted_id)}

    #삭제
    async def delete_member(self,id: int):
        await db.members.delete_one({"id":id})

    #수정 
    async def update_member(self,member_id: int, updated_data: dict):
        await db.members.update_one({"id": member_id}, {"$set": updated_data})

    
    #검색
    async def search_members(self,id: str):
        cursor = db.members.find({"id": id})
        posts = await cursor.to_list(length=100)
        return posts

    async def search_member_by_id(self,id: str):
        return  await db.members.find_one({"id":id})
    
    async def member_login(self, id: str, password: str):
        member= await self.search_member_by_id(id)
        if member is None:
        # 회원이 존재하지 않는 경우의 처리
            return None
        if  member.password==password:
            return  member
        else:
            return "fail"


    
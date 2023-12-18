import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from fastapi import APIRouter
from repository.PostRepository import PostRepository 
router = APIRouter()

repo=PostRepository()

@router.post("/users")
async def read_users(id:str,password:str):
    member = repo.search_member_by_id(id)
    return {"message": "User List"}
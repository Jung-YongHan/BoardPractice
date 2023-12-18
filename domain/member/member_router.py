import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from fastapi import APIRouter,HTTPException, Query
from member_crud import MemberRepository

from starlette.responses import RedirectResponse


router = APIRouter()

repo=MemberRepository()

@router.post("/users")
async def read_users(id:str,password:str):
    member = repo.search_member_by_id(id)
    return {"message": "User List"}

KAKAO_CLIENT_ID = "5f1e26ba70e24642f4243a507d81295c"
KAKAO_REDIRECT_URI = "http://127.0.0.1:8000/auth/kakao"

@router.get("/login/kakao")
async def login_via_kakao():
    return RedirectResponse(
        url=f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={KAKAO_CLIENT_ID}&redirect_uri={KAKAO_REDIRECT_URI}"
    )


"""
@router.get("/auth/kakao")
async def kakao_callback(code: str = Query(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://kauth.kakao.com/oauth/token",
            data={
                "grant_type": "authorization_code",
                "client_id": KAKAO_CLIENT_ID,
                "redirect_uri": KAKAO_REDIRECT_URI,
                "code": code
            }
        )
        response.raise_for_status()
        access_token = response.json().get("access_token")
"""

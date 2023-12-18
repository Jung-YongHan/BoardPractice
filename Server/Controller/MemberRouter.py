import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import httpx
from fastapi import APIRouter,HTTPException, Query
from repository.MemberRepository import MemberRepository 
router = APIRouter()

repo=MemberRepository()

@router.post("/users")
async def read_users(id:str,password:str):
    member = repo.search_member_by_id(id)
    return {"message": "User List"}


@router.get("/kakao")
async def kakao_login(code: Optional[str] = Query(None)):
    try:
        # URL에 포함된 code를 이용하여 액세스 토큰 발급
        access_token = await get_kakao_access_token(code)
        print(access_token)

        # 액세스 토큰을 이용하여 카카오 서버에서 유저 정보(닉네임, 이메일) 받아오기
        user_info = await get_user_info(access_token)
        print("login Controller : ", user_info)

        # DB 처리 및 JWT 반환 로직 구현
        # 예시로 간단히 사용자 정보를 반환합니다.
        return user_info

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

async def get_kakao_access_token(code: str):
    # 카카오 액세스 토큰 발급을 위한 로직을 구현합니다.
    # 이 부분은 카카오 API 문서를 참조하여 구현해야 합니다.
    return "access_token"

async def get_user_info(access_token: str):
    # 카카오 API를 호출하여 사용자 정보를 가져오는 로직을 구현합니다.
    # 이 부분은 카카오 API 문서를 참조하여 구현해야 합니다.
    return {"nickname": "test", "email": "test@example.com"}
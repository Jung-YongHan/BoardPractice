from pydantic import BaseModel,EmailStr,Field



class member_model(BaseModel):
    id:str = Field(None,alias="_id")
    password:str
    name:str
    #email:EmailStr
    kakao_nick_name:str

    
    class Config:
        populate_by_name = True

class loginForm(BaseModel):
    id:str
    password:str

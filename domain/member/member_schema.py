from pydantic import BaseModel,Field


class member_model(BaseModel):
    id: str = Field(..., alias="_id")
    password: str
    name:str

    
    class Config:
        populate_by_name = True

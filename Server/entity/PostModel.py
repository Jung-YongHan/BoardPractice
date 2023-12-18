from datetime import datetime
from pydantic import BaseModel,Field

class PostModel(BaseModel):
    id: int = Field(..., alias="_id")
    title :str
    author: str
    content: str

    
    class Config:
        populate_by_name = True
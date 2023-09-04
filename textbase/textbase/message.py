from pydantic import BaseModel
from typing import List

class Content(BaseModel):
    data_type: str
    value: str

class Message(BaseModel):
    role: str  
    content: List[Content]
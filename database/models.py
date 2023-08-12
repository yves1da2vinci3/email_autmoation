# models.py
from pydantic import BaseModel

class EmailModel(BaseModel):
    object: str
    sender: str
    content: str
    summary: str

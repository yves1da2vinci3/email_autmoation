# endpoints/read.py
from fastapi import HTTPException, APIRouter
from api.crud import read_email

router = APIRouter()

@router.get("/read/{email_id}", response_description="Read an email by ID")
def read_endpoint(email_id: str):
    email = read_email(email_id)
    if email:
        return email
    raise HTTPException(status_code=404, detail="Email not found")

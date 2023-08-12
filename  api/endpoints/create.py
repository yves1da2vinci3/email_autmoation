# endpoints/create.py
from fastapi import HTTPException, APIRouter, Depends
from api.crud import create_email
from database.models import EmailModel

router = APIRouter()

@router.post("/create/", response_description="Create an email")
def create_endpoint(email: EmailModel):
    email_id = create_email(email)
    return {"message": "Email created successfully", "email_id": email_id}

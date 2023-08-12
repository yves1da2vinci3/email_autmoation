# endpoints/update.py
from fastapi import HTTPException, APIRouter, Depends
from api.crud import update_email
from database.models import EmailModel

router = APIRouter()

@router.put("/update/{email_id}", response_description="Update an email by ID")
def update_endpoint(email_id: str, updated_email: EmailModel):
    updated_count = update_email(email_id, updated_email)
    if updated_count > 0:
        return {"message": "Email updated successfully"}
    raise HTTPException(status_code=404, detail="Email not found")

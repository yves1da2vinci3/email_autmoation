# endpoints/delete.py
from fastapi import HTTPException, APIRouter
from api.crud import delete_email

router = APIRouter()

@router.delete("/delete/{email_id}", response_description="Delete an email by ID")
def delete_endpoint(email_id: str):
    deleted_count = delete_email(email_id)
    if deleted_count > 0:
        return {"message": "Email deleted successfully"}
    raise HTTPException(status_code=404, detail="Email not found")

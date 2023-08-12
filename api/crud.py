# crud.py
from typing import List
from bson.objectid import ObjectId
from database.mongodb import emails_collection
from database.models import EmailModel

def create_email(email: EmailModel):
    email_dict = email.dict()
    inserted_email = emails_collection.insert_one(email_dict)
    return str(inserted_email.inserted_id)

def read_email(email_id: str):
    email = emails_collection.find_one({"_id": ObjectId(email_id)})
    if email:
        return EmailModel(**email)
    return None

def update_email(email_id: str, updated_email: EmailModel):
    updated_email_dict = updated_email.dict()
    result = emails_collection.update_one(
        {"_id": ObjectId(email_id)},
        {"$set": updated_email_dict}
    )
    return result.modified_count

def delete_email(email_id: str):
    result = emails_collection.delete_one({"_id": ObjectId(email_id)})
    return result.deleted_count

def list_emails():
    email_list = []
    for email in emails_collection.find():
        email_list.append(EmailModel(**email))
    return email_list

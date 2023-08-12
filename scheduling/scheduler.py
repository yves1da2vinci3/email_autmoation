# scheduler.py
import schedule
import time
from emails.email_retrieval import fetch_emails
from emails.summarization import generate_summary
from database.mongodb import emails_collection
from pdf_generation.pdf_generator import generate_pdf
from pdf_generation.cloudinary_upload import upload_to_cloudinary
from config import CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET

def scheduled_operations():
    # Fetch and process emails
    fetched_emails = fetch_emails()
    for email in fetched_emails:
        summary = generate_summary(email["content"])
        email_data = {
            "object": email["subject"],
            "sender": email["sender_name"],
            "content": email["content"],
            "summary": summary
        }
        emails_collection.insert_one(email_data)
    
    # Generate and upload PDF
    emails_per_day = {}  # Group emails by day
    for email in emails_collection.find():
        email_date = email["_id"].generation_time.date()
        emails_per_day.setdefault(email_date, []).append(email)
    
    pdf_file = generate_pdf(emails_per_day)
    uploaded_url = upload_to_cloudinary(pdf_file)

    if uploaded_url:
        print("PDF uploaded to Cloudinary:", uploaded_url)
    else:
        print("Upload failed")

def start_scheduler():
    schedule.every().day.at("09:00").do(scheduled_operations)
    schedule.every().day.at("22:00").do(scheduled_operations)

    while True:
        schedule.run_pending()
        time.sleep(1)

# Example usage
if __name__ == "__main__":
    start_scheduler()

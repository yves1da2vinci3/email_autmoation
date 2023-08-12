# email_retrieval.py
import smtplib
import email
from email.header import decode_header
from email.utils import parseaddr

def fetch_emails(email_address, email_password, server="imap.example.com", port=993):
    emails = []

    try:
        with smtplib.IMAP4_SSL(server, port) as mail_server:
            mail_server.login(email_address, email_password)
            mail_server.select("inbox")

            _, data = mail_server.search(None, "ALL")
            email_ids = data[0].split()

            for email_id in email_ids:
                _, msg_data = mail_server.fetch(email_id, "(RFC822)")
                msg = email.message_from_bytes(msg_data[0][1])

                subject, encoding = decode_header(msg["subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")

                sender_email, sender_name = parseaddr(msg["from"])
                sender_name, _ = decode_header(sender_name)[0]
                if isinstance(sender_name, bytes):
                    sender_name = sender_name.decode(encoding if encoding else "utf-8")

                content = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            content = part.get_payload(decode=True).decode()

                emails.append({
                    "subject": subject,
                    "sender_name": sender_name,
                    "sender_email": sender_email,
                    "content": content
                })

    except Exception as e:
        print("Error fetching emails:", e)

    return emails

# Example usage
if __name__ == "__main__":
    email_address = "your_email@example.com"
    email_password = "your_email_password"
    fetched_emails = fetch_emails(email_address, email_password)
    for email_data in fetched_emails:
        print("Subject:", email_data["subject"])
        print("Sender:", email_data["sender_name"])
        print("Content:", email_data["content"])
        print("=" * 50)

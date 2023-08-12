# cloudinary_upload.py
import cloudinary
import cloudinary.uploader

def upload_to_cloudinary(pdf_file):
    cloudinary.config(
        cloud_name='YOUR_CLOUD_NAME',
        api_key='YOUR_API_KEY',
        api_secret='YOUR_API_SECRET'
    )

    try:
        response = cloudinary.uploader.upload(pdf_file, resource_type="raw")
        return response["secure_url"]
    except cloudinary.api.Error as e:
        print("Cloudinary upload error:", e)
        return None

# Example usage
if __name__ == "__main__":
    uploaded_url = upload_to_cloudinary("daily_emails.pdf")
    if uploaded_url:
        print("PDF uploaded to Cloudinary:", uploaded_url)
    else:
        print("Upload failed")

# config.py
from decouple import Config, Csv

config = Config()

OPENAI_API_KEY = config('OPENAI_API_KEY')
CLOUDINARY_CLOUD_NAME = config('CLOUDINARY_CLOUD_NAME')
CLOUDINARY_API_KEY = config('CLOUDINARY_API_KEY')
CLOUDINARY_API_SECRET = config('CLOUDINARY_API_SECRET')
MONGODB_URI = config('MONGODB_URI')
MONGODB_DATABASE = config('MONGODB_DATABASE')
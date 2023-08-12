# main.py
from fastapi import FastAPI
from api import endpoints

app = FastAPI()

# Mount the endpoints from the imported modules
app.include_router(create.router)
app.include_router(read.router)
app.include_router(update.router)
app.include_router(delete.router)

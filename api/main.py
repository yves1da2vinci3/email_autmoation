# main.py
from fastapi import FastAPI
from api import endpoints

app = FastAPI()

# Mount the endpoints from the imported modules
app.include_router(endpoints.create.router)
app.include_router(endpoints.read.router)
app.include_router(endpoints.update.router)
app.include_router(endpoints.delete.router)


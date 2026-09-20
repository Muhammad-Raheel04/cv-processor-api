from fastapi import FastAPI
from routes.cv import router as cv_router

app = FastAPI()

@app.get("/")
def root():
    return {"success": "false", "message": "cv processor api is running"}

app.include_router(cv_router)

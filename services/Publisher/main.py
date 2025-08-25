import logging
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return "הכל עובד"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
import logging
from fastapi import FastAPI
from models.config import host
from models.Manager import Manager
from models.logger import get_logger

log = get_logger()

app = FastAPI()

manager = Manager(host)

@app.get("/")
def home():
    try:
        manager.send_to_kafka()

        log.info("send a 20 masages to kafka")
        return "send a 20 masages to kafka"
    
    except Exception as e:

        log.info("fiald to send")
        log.info(f"error:{e}")

        return "fiald to send"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
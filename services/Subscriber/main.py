import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models.config import *
from models.Manager import Manager
from models.logger import get_logger

log = get_logger()

app = FastAPI()

manager = Manager(connection_string , dbname , collection , kafka_host)

@app.get("/")
def home():
    try:
        data = manager.start()
        
        data = [str(d) for d in data]

        return data

        
    
    except Exception as e:

        log.info("fiald to send")
        log.info(f"error:{e}")

        return "fiald to send"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
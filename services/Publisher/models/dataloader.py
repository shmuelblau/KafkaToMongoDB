
from models.logger import get_logger
from sklearn.datasets import fetch_20newsgroups
import json

log = get_logger()
class DataLoader:


    @staticmethod
    def get_all() -> dict[str , list]:
        

        with open("/app/data/data.json" , 'r') as f:
                data = json.load(f)
        
        log.info(f"get a data len = interesting:{len(data['interesting'])} not_interesting:{len(data['not_interesting'])} ")

        return data


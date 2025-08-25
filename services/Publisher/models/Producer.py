
from kafka import KafkaProducer
from models.logger import get_logger

log = get_logger()

class Producer:

    def __init__(self , host ) -> None:
        self.producer = KafkaProducer(
             bootstrap_servers=f'{host}:9092',
             value_serializer=lambda v: v.encode('utf-8')
            )
        

    def send_all(self , all_data:dict):
        for topic , data in all_data.items():
            self.send_to_topic(data , topic)


        
    def send_to_topic(self , data:list , topic ):
        for line in data:
            self.producer.send(topic , line)
        self.producer.flush()
        log.info(f"send a data   topic:{topic}  len:{len(data)}")


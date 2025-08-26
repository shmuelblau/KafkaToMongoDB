
from kafka import KafkaProducer
from models.logger import get_logger

log = get_logger()

class Producer:

    def __init__(self , host ) -> None:
        self.producer = KafkaProducer(
             bootstrap_servers=f'{host}:9092',
             value_serializer=lambda v: v.encode('utf-8'),
             max_block_ms = 120000 ,
             delivery_timeout_ms = 1200000
            )
        try:
            self.producer.send("test" , "test")
            log.info("send a test to kafka")
        except Exception as e:
            log.info("fild send test")
            log.info(e)

        

    def send_all(self , all_data:dict):
        for topic , data in all_data.items():
            print(f"topic:{topic} ")
            self.send_to_topic(data , topic)


        
    def send_to_topic(self , data:list , topic ):
        log.info(f"try send to topik : {topic} len :{len(data)}")
        for line in data:
            
            self.producer.send(topic , line)
        self.producer.flush()
        log.info(f"send a data topic:{topic}  len:{len(data)}")


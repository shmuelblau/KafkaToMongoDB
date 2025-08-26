from kafka import KafkaConsumer
import time

class Consumer:

    def __init__(self ,kafka_host,  topic) -> None:
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=f'{kafka_host}:9092',
            auto_offset_reset='earliest',
            group_id = topic,
            value_deserializer=lambda v: v.decode('utf-8'),
            consumer_timeout_ms=10000
            
        )


    def get_data(self) -> list:
        
        result = []

        self.consumer

        for i in self.consumer:
            result.append(i.value)

        return result


    
        
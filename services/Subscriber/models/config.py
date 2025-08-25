import os 

kafka_host = os.getenv("KAFKA_HOST" , "kafka")

dbname = os.getenv("DATABASE" , "fromkafka")
collection = os.getenv('COLLECTION',"interesting")
connection_string = os.getenv("CONNECTION_STRING" ,"mongodb://shmuel:1234@mongo:27017/fromkafka?authSource=admin")


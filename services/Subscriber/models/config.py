import os 

host = os.getenv("HOST" , "kafka")
user = os.getenv("USER" , "shmuel")
password = os.getenv("PASSWORD" , "1234")
dbname = os.getenv("DATABASE" , "iran")
collection = os.getenv('COLLECTION',"tweets")
connection_string = os.getenv("CONNECTION_STRING" ,"mongodb://shmuel:1234@mongo:27017/iran?authSource=admin")

iran_collection_name = os.getenv("IRAN_COLLECTION_NAME","tweets")
iran_db_name = os.getenv("IRAN_DB_NAME" ,"IranMalDB")
iran_connection_string = os.getenv("IRAN_CONNECTION_STRING" ,"mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/")
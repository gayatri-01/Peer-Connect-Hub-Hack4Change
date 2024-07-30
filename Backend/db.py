from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()

MONGO_URI  = "mongodb+srv://admin:admin@cluster0.wdpxeyv.mongodb.net/?retryWrites=true&w=majority&appName=eduforge"


#MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.eduforge
users = db.users
permap = db.personMappings
feedback = db.feedback
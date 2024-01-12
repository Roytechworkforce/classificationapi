from pymongo import MongoClient
import os
client=MongoClient("mongodb://localhost:27017" if os.name=="nt" else "mongodb://db:27017" )

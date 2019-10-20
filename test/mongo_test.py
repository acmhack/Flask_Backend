import pymongo
from pprint import pprint
import dns

client = pymongo.MongoClient("mongodb+srv://Dev-Admin:<password>@pickhacks-alesk.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

serverStatusResult = db.command('serverStatus')
pprint(serverStatusResult)


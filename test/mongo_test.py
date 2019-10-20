import pymongo
from pprint import pprint
import dns

client = pymongo.MongoClient("mongodb+srv://pickhacks:__pickhacksdb2019__@test-hv3v4.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

serverStatusResult = db.command('serverStatus')
pprint(serverStatusResult)


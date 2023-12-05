import pymongo
from bson import ObjectId

conn = pymongo.MongoClient('mongodb+srv://coffee:x6wzfdrxhv6AVgyC@cluster0.jnw32.mongodb.net/')

db = conn.coffee_shop
customers_coll = db.customers

# customers_coll.update_one({"_id": ObjectId("656f12c77c9b40397beefc5a")}, {"$set": {"phone_number": "1111111"}})

customers_coll.update_many({"last_name": "Wilson"}, {"$set": {"phone_number": "222222222"}})
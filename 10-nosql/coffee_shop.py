import pymongo

conn = pymongo.MongoClient('mongodb+srv://coffee:x6wzfdrxhv6AVgyC@cluster0.jnw32.mongodb.net/')

db = conn.coffee_shop
customers_coll = db.customers

customers = customers_coll.find({})

print(customers)

for c in customers:
    print(c)

new_customer = {'first_name': 'Suzan', 'last_name': 'Wilson', 'phone_number': '0987654'}
result = customers_coll.insert_one(new_customer)
print(result)


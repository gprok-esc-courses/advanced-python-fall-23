from faker import Faker
import mysql.connector
import faker_commerce
import random

db = mysql.connector.connect(
    host='localhost', user='test', password='test', database='shop_adv_py'
)

cursor = db.cursor()
faker_gen = Faker()
faker_gen.add_provider(faker_commerce.Provider)


# query = "INSERT INTO customers(name, phone) VALUES (%s, %s)"
#
# for i in range(100):
#     values = (faker_gen.name(), faker_gen.phone_number())
#
#     cursor.execute(query, values)

cursor.execute("SELECT id FROM customers")
result = cursor.fetchall()
ids = []
for item in result:
    ids.append(item[0])
print(ids)


query = "INSERT INTO orders (product, price, customers_id) VALUES (%s, %s, %s)"

for i in range(100):
    x = random.randint(1, len(ids))
    values = (faker_gen.ecommerce_name(), random.randint(10, 350), ids[x])
    cursor.execute(query, values)

db.commit()

# print(cursor.rowcount)
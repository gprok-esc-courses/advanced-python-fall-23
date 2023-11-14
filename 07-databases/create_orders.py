from faker import Faker
import mysql.connector
import random

db = mysql.connector.connect(
    host='localhost', user='test', password='test', database='advanced_python'
)

cursor = db.cursor()
faker_gen = Faker()

query = "INSERT INTO orders(order_date, price, customers_id) VALUES (%s, %s, %s)"

for i in range(100):
    values = (faker_gen.date(), random.uniform(10.0, 1000.0), random.randint(1, 103))

    cursor.execute(query, values)

db.commit()

print(cursor.rowcount)
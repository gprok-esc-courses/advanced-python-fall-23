from faker import Faker
import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='test', password='test', database='advanced_python'
)

cursor = db.cursor()
faker_gen = Faker()

query = "INSERT INTO customers(name, subscr_date, email) VALUES (%s, %s, %s)"

for i in range(100):
    values = (faker_gen.name(), faker_gen.date(), faker_gen.email())

    cursor.execute(query, values)

db.commit()

print(cursor.rowcount)
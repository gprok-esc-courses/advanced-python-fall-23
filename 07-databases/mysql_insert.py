import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='test', password='test', database='advanced_python'
)

cursor = db.cursor()

query = "INSERT INTO customers(name, subscr_date, email) VALUES (%s, %s, %s)"
values = ('Mike Smith', '2023-04-11', 'ms@test.xyz')

cursor.execute(query, values)

db.commit()

print(cursor.rowcount)
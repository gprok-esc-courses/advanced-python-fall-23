import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='test', password='test', database='sakila', port='3307'
)

cursor = db.cursor()

cursor.execute("SELECT * FROM actor")

data = cursor.fetchall()

for row in data:
    print(row[1])


import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='test', password='test', database='sakila'
)

cursor = db.cursor()

cursor.execute("SELECT * FROM actor")

data = cursor.fetchall()

for row in data:
    print(row[2])
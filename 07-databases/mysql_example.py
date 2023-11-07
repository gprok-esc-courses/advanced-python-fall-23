import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='test', password='test', database='advanced_python'
)

cursor = db.cursor()

cursor.execute("SELECT * FROM customers")

data = cursor.fetchall()

for row in data:
    print(row[1])

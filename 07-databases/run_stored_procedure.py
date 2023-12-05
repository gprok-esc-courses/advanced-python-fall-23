import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='test', password='test', database='sample'
)

cursor = db.cursor()

cursor.callproc('GetAllPersons')

data = cursor.stored_results()

for row in data:
    people = row.fetchall()

    for person in people:
        print(person)


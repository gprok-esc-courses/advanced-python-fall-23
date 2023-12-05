import mysql.connector
from models import Actor

db = mysql.connector.connect(
    host='localhost', user='test', password='test', database='sakila'
)

cursor = db.cursor()

cursor.execute("SELECT * FROM actor")

data = cursor.fetchall()

actors = []

for row in data:
    actor = Actor(row[0], row[1], row[2], row[3], row[4])
    actors.append(actor)


for actor in actors:
    print(actor.last_name)


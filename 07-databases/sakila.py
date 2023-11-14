import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='test', password='test', database='sakila'
)

cursor = db.cursor()

cursor.execute("""SELECT a.first_name, a.last_name, COUNT(*) FROM actor a
INNER JOIN film_actor fa ON a.actor_id=fa.actor_id
INNER JOIN film f ON f.film_id=fa.film_id
GROUP BY a.actor_id
HAVING COUNT(*) > 20
ORDER BY a.last_name DESC""")

data = cursor.fetchall()

for row in data:
    print(row)
import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='test', password='test', database='advanced_python'
)

cursor = db.cursor()

cursor.execute("""SELECT customers.name, COUNT(*), SUM(orders.price) FROM customers
LEFT JOIN orders ON customers.id=orders.customers_id
GROUP BY customers.id
HAVING SUM(orders.price) IS NOT null AND SUM(orders.price) < 300""")

data = cursor.fetchall()

for row in data:
    print(row)

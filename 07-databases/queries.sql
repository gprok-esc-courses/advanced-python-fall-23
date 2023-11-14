# Join tables selecting from both tables
SELECT * FROM customers, orders
WHERE customers.id=orders.customers_id
AND customers_id=1;

# INNER JOIN
SELECT * FROM customers
INNER JOIN orders ON customers.id=orders.customers_id
WHERE customers.id=1;

# LEFT JOIN get customer even they have no orders
SELECT * FROM customers
LEFT JOIN orders ON customers.id=orders.customers_id
WHERE customers.id=104;

# Aggregate functions
SELECT SUM(orders.price) FROM customers
INNER JOIN orders ON customers.id=orders.customers_id
WHERE customers.id=1;

# Group by and Having
SELECT customers.name, COUNT(*), SUM(orders.price) FROM customers
LEFT JOIN orders ON customers.id=orders.customers_id
GROUP BY customers.id
HAVING SUM(orders.price) IS NOT null AND SUM(orders.price) < 300;
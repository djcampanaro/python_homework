import sqlite3

def run_query(query, cur, *args, full_row=False):
    try:
        cur.execute(query, *args)
        results = cur.fetchall()
        if full_row:
            for row in results:
                print(row)
            return results
        else:
            results_list = [r[0] for r in results]
            return results_list
    except Exception as e:
        print('Error: ', e)

DB_PATH = '../db/lesson.db'

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("PRAGMA foreign_keys = ON;")

# TASK 1: Complex JOINs with Aggregation

query = """
SELECT o.order_id, ROUND(SUM(p.price * li.quantity), 2) AS total_price
FROM orders AS o
JOIN line_items AS li ON li.order_id = o.order_id
JOIN products AS p ON p.product_id = li.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5
"""

run_query(query, cur, full_row=True)

# Task 2: Understanding Subqueries

query = """
SELECT customer_name, ROUND(AVG(t.total_price)) AS average_total_price
FROM customers AS c
LEFT JOIN (
    SELECT customer_id AS customer_id_b, ROUND(SUM(p.price * li.quantity), 2) AS total_price
    FROM orders AS o
    JOIN line_items AS li ON li.order_id = o.order_id
    JOIN products AS p ON p.product_id = li.product_id
    GROUP BY o.order_id
    ) AS t
ON t.customer_id_b = c.customer_id
GROUP BY c.customer_id;
"""

run_query(query, cur, full_row=True)

# Task 3: An Insert Transaction Based on Data        

customer_id = run_query("SELECT customer_id FROM customers c WHERE c.customer_name = 'Perez and Sons';", cur)[0]
employee_id = run_query("SELECT employee_id FROM employees e WHERE (e.first_name || ' ' || e.last_name) = 'Miranda Harris';", cur)[0]
least_expens_products = run_query("SELECT product_id FROM products p ORDER BY p.price ASC LIMIT 5", cur)

try:
    cur.execute("INSERT INTO orders (customer_id, employee_id, date) VALUES (?, ?, JULIANDAY('now')) RETURNING order_id", (customer_id, employee_id))
    order_id = cur.fetchall()[0][0]
    products_list = [(order_id, p, 10) for p in least_expens_products]

    cur.executemany("INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?);", products_list)
    conn.commit()

except Exception as e:
    conn.rollback()
    print('Error: ', e)

query = """
SELECT line_item_id, quantity, p.product_name
FROM line_items li
JOIN products p ON li.product_id = p.product_id
WHERE li.order_id = ?;
"""

run_query(query, cur, (order_id,), full_row=True)

# Task 4: Aggregation with HAVING

query = """
SELECT e.employee_id, first_name, last_name, COUNT(o.order_id) as count_of_orders
FROM employees AS e
JOIN orders AS o ON o.employee_id = e.employee_id
GROUP BY e.employee_id
HAVING COUNT(o.order_id) > 5;
"""

run_query(query, cur, full_row=True)

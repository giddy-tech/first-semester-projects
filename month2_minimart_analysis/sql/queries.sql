-- SQL queries for retrieving insights

-- 1. Retrieve all customers
SELECT * FROM customers;

-- 2. Retrieve all products
SELECT * FROM products;

-- 3. Filter products by category
SELECT * FROM products WHERE category = 'Drinks';

-- 4. List recent orders by date
SELECT * FROM orders ORDER BY order_date DESC;

-- 5. Count total orders
SELECT COUNT(*) AS total_orders FROM orders;

-- 6. Revenue per product (price * quantity)
SELECT 
    p.product_name,
    SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name;

-- 7. Average product price
SELECT AVG(price) AS avg_price FROM products;

-- 8. Detailed order info with INNER JOIN
SELECT 
    o.order_id,
    c.name AS customer_name,
    p.product_name,
    o.quantity,
    (o.quantity * p.price) AS total_price,
    o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id;

-- 9. List all customers with their orders (LEFT JOIN)
SELECT 
    c.customer_id,
    c.name AS customer_name,
    o.order_id,
    o.product_id,
    o.quantity,
    o.order_date
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

-- 10. List all products, even if not ordered (LEFT JOIN)
SELECT 
    p.product_id,
    p.product_name,
    o.order_id,
    o.quantity
FROM products p
LEFT JOIN orders o ON p.product_id = o.product_id;

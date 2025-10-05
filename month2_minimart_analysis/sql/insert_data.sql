-- SQL script to insert sample data
-- SQL script to insert sample data

-- Customers
INSERT INTO customers (name, email, join_date) VALUES
('Alice', 'alice@altschoolafrica', '2025-01-10'),
('Bob', 'bob@altschoolafrica', '2025-02-05'),
('Charlie', 'charlie@altschoolafrica', '2025-03-12'),
('Diana', 'diana@altschoolafrica', '2025-04-01'),
('Eve', 'eve@altschoolafrica', '2025-04-15');

-- Products
INSERT INTO products (product_name, category, price) VALUES
('Coke', 'Drinks', 2.50),
('Pepsi', 'Drinks', 2.50),
('Bread', 'Food', 3.00),
('Milk', 'Dairy', 2.00),
('Cheese', 'Dairy', 4.50);

-- Orders
INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 1, 3, '2025-04-01'),
(2, 3, 2, '2025-04-02'),
(1, 4, 1, '2025-04-03'),
(3, 5, 2, '2025-04-04'),
(4, 2, 5, '2025-04-05');


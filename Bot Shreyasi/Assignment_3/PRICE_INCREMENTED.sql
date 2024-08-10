CREATE DATABASE shop;

USE shop;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

INSERT INTO products (name, price) VALUES ('Product A', 100.00);
INSERT INTO products (name, price) VALUES ('Product B', 150.00);
INSERT INTO products (name, price) VALUES ('Product C', 200.00);

UPDATE products
SET price = price * 1.10;

SELECT name, price AS new_price
FROM products;

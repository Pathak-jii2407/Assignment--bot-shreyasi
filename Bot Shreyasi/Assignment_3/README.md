🛒 Shop Database Schema and Sample Data
Overview
This SQL script sets up a basic database for a shop, creates a table for products, inserts sample data, and updates the prices of the products. Finally, it retrieves the updated product information.

Steps
1. Create Database
sql
Copy code
CREATE DATABASE shop;
Description:

Creates a new database named shop.
2. Use the Database
sql
Copy code
USE shop;
Description:

Selects the shop database for subsequent operations.
3. Create Products Table
sql
Copy code
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
Description:

Creates a table named products with the following columns:
id: A unique identifier for each product (automatically incremented).
name: The name of the product (cannot be null).
price: The price of the product (cannot be null, with two decimal places).
4. Insert Sample Data
sql
Copy code
INSERT INTO products (name, price) VALUES ('Product A', 100.00);
INSERT INTO products (name, price) VALUES ('Product B', 150.00);
INSERT INTO products (name, price) VALUES ('Product C', 200.00);
Description:

Adds three sample products to the products table with their respective prices.
5. Update Product Prices
sql
Copy code
UPDATE products
SET price = price * 1.10;
Description:

Increases the price of all products by 10%.
6. Retrieve Updated Product Information
sql
Copy code
SELECT name, price AS new_price
FROM products;
Description:

Retrieves the names and updated prices of all products. The price column is aliased as new_price in the output.
Example Output
plaintext
Copy code
+-------------+-----------+
| name        | new_price |
+-------------+-----------+
| Product A   | 110.00    |
| Product B   | 165.00    |
| Product C   | 220.00    |

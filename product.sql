
CREATE DATABASE product;

-- Use the database
USE product;

-- Create the products table
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

-- Insert sample data
INSERT INTO products (name, price) VALUES
('Laptop', 50000.00),
('Mouse', 800.00),
('Keyboard', 1500.00);

-- Display the data
SELECT * FROM products;
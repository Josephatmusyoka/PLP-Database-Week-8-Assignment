-- Insert sample data into the Users table
INSERT INTO users (username, password, role, email, phone) VALUES
('admin', 'adminpassword123', 'admin', 'admin@umojafashion.com', '0712345678'),
('employee1', 'emp1password', 'employee', 'emp1@umojafashion.com', '0712345679');

-- Insert sample data into the Suppliers table
INSERT INTO suppliers (name, contact_name, email, phone, address) VALUES
('Supplier A', 'John Doe', 'supplierA@company.com', '0723456789', '123 Fashion Street, Nairobi'),
('Supplier B', 'Jane Smith', 'supplierB@company.com', '0734567890', '456 Apparel Avenue, Mombasa');

-- Insert sample data into the Customers table
INSERT INTO customers (first_name, last_name, email, phone, address) VALUES
('Mary', 'Mwangi', 'mary.mwangi@example.com', '0745678901', '789 Boutique Road, Nairobi'),
('Joseph', 'Otieno', 'joseph.otieno@example.com', '0745678902', '321 Tailor Lane, Kisumu');

-- Insert sample data into the Items table
INSERT INTO items (name, description, quantity, price, supplier_id) VALUES
('Red Dress', 'Elegant red dress for evening wear', 10, 4999.99, 1),
('Blue Jeans', 'Comfortable blue jeans for casual wear', 20, 2499.99, 2),
('Black Shoes', 'Stylish black leather shoes', 15, 3500.00, 1),
('White Shirt', 'Cotton white shirt for formal wear', 25, 1500.00, 2);

-- Insert sample data into the Sales table
INSERT INTO sales (customer_id, item_id, quantity, total_price) VALUES
(1, 1, 2, 9999.98),  -- Mary buys 2 Red Dresses
(2, 3, 1, 3500.00);  -- Joseph buys 1 Black Shoes

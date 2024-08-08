

-- Sample data for Customer table
-- Columns (customer_id, customer_name, customer_tel)
(1, 'Alice', '123-456-7890'),
(2, 'Bob', '234-567-8901'),
(3, 'Charlie', '345-678-9012');

-- Sample data for Product table
-- columns (product_id, product_name, category, price)
(1, 'Widget', 'Widgets', 10.00),
(2, 'Gadget', 'Gadgets', 20.00),
(3, 'Doohickey', 'Doohickeys', 15.00);

-- Sample data for Orders table
-- columns (customer_id, product_id, order_date, quantity, total_amount) 
(1, 1, '2023-05-01', 2, 20.00),
(1, 2, '2023-05-02', 1, 20.00),
(2, 1, '2023-05-03', 3, 30.00),
(2, 3, '2023-05-04', 1, 15.00),
(3, 2, '2023-05-05', 2, 40.00),
(3, 3, '2023-05-06', 1, 15.00),
(3, 1, '2023-05-07', 1, 10.00);
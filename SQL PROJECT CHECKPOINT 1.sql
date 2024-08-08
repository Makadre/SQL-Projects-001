--- 1.	Implement the provided relation model using SQL ( DDL part )
CREATE DATABASE CUSTOMERPRODUCT

CREATE TABLE CUSTOMER (
    CUSTOMER_ID INT PRIMARY KEY,
	CUSTOMER_NAME VARCHAR (255),
	CUSTOMER_TEL VARCHAR (255)
);

CREATE TABLE PRODUCT (
    PRODUCT_ID INT PRIMARY KEY,
	PRODUCT_NAME VARCHAR (255),
	CATEGORY VARCHAR (255),
	PRICE DECIMAL (7,2) CHECK (PRICE>0) 
);

CREATE TABLE ORDERS (
	CUSTOMER_ID INT FOREIGN KEY REFERENCES CUSTOMER (CUSTOMER_ID),
	PRODUCT_ID INT FOREIGN KEY REFERENCES PRODUCT (PRODUCT_ID),
	ORDER_DATE DATE,
    QUANTITY INT,
	TOTAL_AMOUNT INT
);
DROP TABLE ORDERS;
--- 2.	Insert data into your tables ( DML part )
INSERT INTO CUSTOMER VALUES (1, 'Alice', '123-456-7890'),
(2, 'Bob', '234-567-8901'),
(3, 'Charlie', '345-678-9012');

INSERT INTO PRODUCT VALUES (1, 'Widget', 'Widgets', 10.00),
(2, 'Gadget', 'Gadgets', 20.00),
(3, 'Doohickey', 'Doohickeys', 15.00);

INSERT INTO ORDERS VALUES (1, 1, '2023-05-01', 2, 20.00),
(1, 2, '2023-05-02', 1, 20.00),
(2, 1, '2023-05-03', 3, 30.00),
(2, 3, '2023-05-04', 1, 15.00),
(3, 2, '2023-05-05', 2, 40.00),
(3, 3, '2023-05-06', 1, 15.00),
(3, 1, '2023-05-07', 1, 10.00);

--- 3.	Write a SQL query to retrieve the names of the customers who have placed an order for at least one widget and at least one gadget, along with the total cost of the widgets and gadgets ordered by each customer. The cost of each item should be calculated by multiplying the quantity by the price of the product.
SELECT CUSTOMER.CUSTOMER_NAME,
       SUM(ORDERS.QUANTITY * PRODUCT.PRICE) AS total_cost
FROM CUSTOMER
JOIN ORDERS ON CUSTOMER.CUSTOMER_ID = ORDERS.CUSTOMER_ID
JOIN PRODUCT  ON ORDERS.PRODUCT_ID = PRODUCT.PRODUCT_ID
WHERE PRODUCT.PRODUCT_NAME IN ('WIDGET', 'GADGET')
GROUP BY CUSTOMER.CUSTOMER_ID, CUSTOMER.CUSTOMER_NAME
HAVING COUNT(DISTINCT CASE WHEN PRODUCT.PRODUCT_NAME = 'WIDGET' THEN ORDERS.PRODUCT_ID END) > 0
   AND COUNT(DISTINCT CASE WHEN PRODUCT.PRODUCT_NAME = 'GADGET' THEN ORDERS.PRODUCT_ID END) > 0;

--- 4.	Write a query to retrieve the names of the customers who have placed an order for at least one widget, along with the total cost of the widgets ordered by each customer.
SELECT CUSTOMER.CUSTOMER_NAME,
       SUM(ORDERS.QUANTITY * PRODUCT.PRICE) AS total_cost
FROM CUSTOMER
JOIN ORDERS ON CUSTOMER.CUSTOMER_ID = ORDERS.CUSTOMER_ID
JOIN PRODUCT  ON ORDERS.PRODUCT_ID = PRODUCT.PRODUCT_ID
WHERE PRODUCT.PRODUCT_NAME = 'WIDGET'
GROUP BY CUSTOMER.CUSTOMER_ID, CUSTOMER.CUSTOMER_NAME;

--- 5.	Write a query to retrieve the names of the customers who have placed an order for at least one gadget, along with the total cost of the gadgets ordered by each customer.
SELECT CUSTOMER.CUSTOMER_NAME,
       SUM(ORDERS.QUANTITY * PRODUCT.PRICE) AS total_cost
FROM CUSTOMER
JOIN ORDERS ON CUSTOMER.CUSTOMER_ID = ORDERS.CUSTOMER_ID
JOIN ORDERS ON CUSTOMER.CUSTOMER_ID = PRODUCT.PRODUCT_ID
JOIN PRODUCT  ON ORDERS.PRODUCT_ID = PRODUCT.PRODUCT_ID
WHERE PRODUCT.PRODUCT_NAME = 'GADGET'
GROUP BY CUSTOMER.CUSTOMER_ID, CUSTOMER.CUSTOMER_NAME;

--- 6.	Write a query to retrieve the names of the customers who have placed an order for at least one doohickey, along with the total cost of the doohickeys ordered by each customer.
SELECT CUSTOMER.CUSTOMER_NAME, SUM(ORDERS.QUANTITY * PRODUCT.PRICE) AS total_cost
FROM CUSTOMER
JOIN ORDERS ON CUSTOMER.CUSTOMER_ID = ORDERS.CUSTOMER_ID
JOIN order_items oi ON o.order_id = oi.order_id
JOIN PRODUCT  ON ORDERS.PRODUCT_ID = PRODUCT.PRODUCT_ID
WHERE PRODUCT.PRODUCT_NAME = 'DOOHICKEY'
GROUP BY CUSTOMER.CUSTOMER_ID, CUSTOMER.CUSTOMER_NAME;

--- 7.	Write a query to retrieve the total number of widgets and gadgets ordered by each customer, along with the total cost of the orders.
SELECT CUSTOMER.CUSTOMER_NAME,
       SUM(CASE WHEN PRODUCT.PRODUCT_NAME IN ('WIDGET', 'GADGET') THEN ORDERS.QUANTITY ELSE 0 END) AS total_quantity,
       SUM(ORDERS.QUANTITY * PRODUCT.PRICE) AS total_cost
FROM CUSTOMER
JOIN ORDERS ON CUSTOMER.CUSTOMER_ID = ORDERS.CUSTOMER_ID
JOIN PRODUCT  ON ORDERS.PRODUCT_ID = PRODUCT.PRODUCT_ID
WHERE PRODUCT.PRODUCT_NAME IN ('WIDGET', 'GADGET')
GROUP BY CUSTOMER.CUSTOMER_ID, CUSTOMER.CUSTOMER_NAME;

--- 8.	Write a query to retrieve the names of the products that have been ordered by at least one customer, along with the total quantity of each product ordered.
SELECT PRODUCT.PRODUCT_NAME, SUM(ORDERS.QUANTITY) AS TOTALQUANTITY
FROM PRODUCT 
JOIN ORDERS ON PRODUCT.PRODUCT_ID = ORDERS.PRODUCT_ID
GROUP BY PRODUCT.PRODUCT_ID, PRODUCT.PRODUCT_NAME;

--- 9.	Write a query to retrieve the names of the customers who have placed the most orders, along with the total number of orders placed by each customer.
-- Find the maximum number of orders placed by any customer
WITH ORDERSCOUNTS AS (
    SELECT CUSTOMER.CUSTOMER_NAME,
           COUNT(o.order_id) AS order_count
    FROM CUSTOMER
    JOIN ORDERS ON CUSTOMER.CUSTOMER_ID = ORDERS.CUSTOMER_ID
    GROUP BY CUSTOMER.CUSTOMER_ID, CUSTOMER.CUSTOMER_NAME
),
MAXORDERCOUNT AS (
    SELECT MAX(ORDERS_COUNT) AS MAX_ORDERS
    FROM ORDERSCOUNTS
)
-- Retrieve customers with the maximum order count
SELECT CUSTOMER_NAME,
       ORDERS_COUNT
FROM ORDERS
WHERE ORDERS_COUNT = (SELECT max_orders FROM MaxOrderCount);

--- 10.	Write a query to retrieve the names of the products that have been ordered the most, along with the total quantity of each product ordered.
SELECT PRODUCT.PRODUCT_NAME, SUM(ORDERS.QUANTITY) AS TOTAL_QUANTITY
FROM PRODUCT
JOIN ORDERS ON PRODUCT.PRODUCT_ID = ORDERS.PRODUCT_ID
GROUP BY PRODUCT.PRODUCT_ID, PRODUCT.PRODUCT_NAME
ORDER BY TOTAL_QUANTITY DESC;

--- 11.	Write a query to retrieve the names of the customers who have placed an order on every day of the week, along with the total number of orders placed by each customer.
WITH OrderDays AS (
    SELECT CUSTOMER.CUSTOMER_ID,
           CUSTOMER.CUSTOMER_NAME,
           EXTRACT(DOW FROM ORDERS.ORDER_DATE) AS DAY_OF_WEEK
    FROM CUSTOMER
    JOIN ORDERS ON CUSTOMER.CUSTOMER_ID = ORDERS.CUSTOMER_ID
),
CUSTOMERORDERDAYS AS (
    SELECT CUSTOMER_ID,
           CUSTOMER_NAME,
           COUNT(DISTINCT DAY_OF_WEEK) AS NUM_DAYS
    FROM ORDERS
    GROUP BY CUSTOMER_ID,
           CUSTOMER_NAME
)
SELECT CUSTOMER_NAME,
       COUNT(ORDERS.QUANTITY) AS TOTALORDERS
FROM CUSTOMER
JOIN ORDERS ON CUSTOMER.CUSTOMER_ID = ORDERS.CUSTOMER_ID
JOIN CustomerOrderDays cod ON cCUSTOMER.CUSTOMER_ID = cod.CUSTOMER_ID
WHERE cod.num_days = 7
GROUP BY CUSTOMER.CUSTOMER_ID, CUSTOMER.CUSTOMER_NAME;

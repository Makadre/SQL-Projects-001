CREATE DATABASE CUSTOMER

CREATE TABLE CUSTOMERS (
    CUSTOMER_ID INT NOT NULL PRIMARY KEY,
	NAME VARCHAR (255) NOT NULL,
	ADDRESS VARCHAR (255) NOT NULL
);

CREATE TABLE PRODUCTS (
    PRODUCT_ID INT NOT NULL PRIMARY KEY,
	NAME VARCHAR (255) NOT NULL,
	PRICE DECIMAL (7,2) CHECK (PRICE>0) NOT NULL
);


CREATE TABLE ORDERS (
    ORDER_ID INT NOT NULL PRIMARY KEY,
	CUSTOMER_ID INT NOT NULL FOREIGN KEY REFERENCES CUSTOMERS (CUSTOMER_ID),
	PRODUCT_ID INT NOT NULL FOREIGN KEY REFERENCES PRODUCTS (PRODUCT_ID),
	QUANTITY INT NOT NULL,
	ORDER_DATE DATE NOT NULL
);


DML
-- Write the appropriate SQL queries to insert all the provided records in their corresponding tables.

INSERT INTO PRODUCTS (PRODUCT_ID, NAME, PRICE)
VALUES (1, 'COOKIES', '10'),
(2, 'CANDY', '5.2');

INSERT INTO CUSTOMERS (CUSTOMER_ID, NAME, ADDRESS)
VALUES (1, 'AHMED', 'TUNISIA'), 
(2, 'COULIBALY', 'SENEGAL'),
(3, 'HASSAN','EGYPT');

INSERT INTO ORDERS (ORDER_ID, CUSTOMER_ID, PRODUCT_ID, QUANTITY, ORDER_DATE)
VALUES (1, 1, 1, 3, '2023-01-22'), (2, 2, 2, 10, '2023-04-14');


-- Update the quantity of the second order, the new value should be 6.

UPDATE ORDERS
SET QUANTITY = 6
WHERE ORDER_ID = 2;

-- Delete the third customer from the customers table.

DELETE FROM CUSTOMERS WHERE CUSTOMER_ID = 3;

-- Delete the orders table content then drop the table.

DELETE FROM ORDERS WHERE ORDER_ID IN (1,2);
DROP TABLE ORDERS



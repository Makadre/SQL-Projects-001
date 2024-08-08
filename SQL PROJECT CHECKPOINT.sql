
--- 1.	Convert the given entity-relationship diagram into a relational model.
CREATE DATABASE WINEPRODUCTION;


--- 2.	Implement the relational model using SQL.
CREATE TABLE WINE (
NUMW INT PRIMARY KEY,
CATEGORY VARCHAR (255),
YEAR INT,
DEGREE DECIMAL );

CREATE TABLE PRODUCER (
NUMP INT PRIMARY KEY,
FIRSTNAME VARCHAR (255),
LASTNAME VARCHAR (255),
REGION VARCHAR (255) );

CREATE TABLE HARVEST (
NUMW INT FOREIGN KEY REFERENCES WINE (NUMW),
NUMP INT FOREIGN KEY REFERENCES PRODUCER (NUMP),
QUANTITY INT );


--- 3.	Insert into
INSERT INTO WINE VALUES (1, 'Red', 2018, 13.5),
    (2, 'White', 2020, 11.8),
    (3, 'Rosé', 2019, 12.2),
	(4, 'Red', 2017, 14.0),
    (5, 'White', 2019, 10.5),
    (6, 'Rosé', 2021, 11.7),
    (7, 'Red', 2022, 13.3),
    (8, 'White', 2023, 11.0),
    (9, 'Rosé', 2022, 12.5),
	(10, 'Red', 2023, 13.2),
    (11, 'White', 2022, 11.5),
    (12, 'Rosé', 2021, 12.8),
    (13, 'Red', 2020, 14.3),
    (14, 'White', 2019, 10.7),
    (15, 'Rosé', 2022, 11.9),
    (16, 'Red', 2018, 13.6),
    (17, 'White', 2021, 11.2),
    (18, 'Rosé', 2020, 12.1),
    (19, 'Red', 2019, 14.5),
    (20, 'White', 2023, 10.9);

	INSERT INTO PRODUCER VALUES (101, 'John', 'Smith', 'Bordeaux'),
    (102, 'Maria', 'Garcia', 'Sousse'),
    (103, 'Alex', 'Lee', 'Champagne'),
	(104, 'Emily', 'Johnson', 'Burgundy'),
    (105, 'Daniel', 'Martinez', 'Sousse'),
    (106, 'Sophia', 'Kim', 'Champagne'),
    (107, 'Oliver', 'Brown', 'Bordeaux'),
    (108, 'Emma', 'Nguyen', 'Alsace'),
    (109, 'Liam', 'Rodriguez', 'Sousse'),
	(110, 'Sophie', 'Brown', 'Bordeaux'),
    (111, 'William', 'Nguyen', 'Alsace'),
    (112, 'Emma', 'Rodriguez', 'Sousse'),
    (113, 'James', 'Kim', 'Champagne'),
    (114, 'Olivia', 'Martinez', 'Burgundy'),
    (115, 'Noah', 'Johnson', 'Bordeaux'),
    (116, 'Ava', 'Garcia', 'Sousse'),
    (117, 'Liam', 'Lee', 'Champagne'),
    (118, 'Isabella', 'Smith', 'Burgundy'),
    (119, 'Ethan', 'Jones', 'Alsace'),
    (120, 'Mia', 'Davis', 'Bordeaux');

	INSERT INTO HARVEST VALUES (1, 101, 500),  
    (2, 102, 300),  
    (3, 103, 700),
	(4, 104, 600),   
    (5, 105, 400),  
    (6, 106, 550),   
    (7, 107, 480),  
    (8, 108, 620),  
    (9, 109, 520),
    (10, 110, 550),  
    (11, 111, 420),  
    (12, 112, 680), 
    (13, 113, 590),  
    (14, 114, 380),  
    (15, 115, 520),  
    (16, 116, 610),  
    (17, 117, 450), 
    (18, 118, 700),  
    (19, 119, 560),  
    (20, 120, 400);

--- 4.	Give the list the producer
SELECT NUMP, FIRSTNAME, LASTNAME FROM PRODUCER;

--- 5.	Give the list of producers sorted by name.
SELECT FIRSTNAME, LASTNAME FROM PRODUCER;

--- 6.	Give the list the producers of Sousse.
SELECT * FROM PRODUCER
WHERE REGION = 'SOUSSE';

--- 7.	Calculate the total quantity of wine produced having the number 12.
SELECT WINE.NUMW, 
SUM(HARVEST.QUANTITY) AS total_quantity
FROM wine
JOIN HARVEST ON WINE.NUMW = HARVEST.NUMW
WHERE quantity = 12;

--- 8.	Calculate the quantity of wine produced by category.
SELECT WINE.CATEGORY FROM WINE
JOIN HARVEST ON WINE.NUMW = HARVEST.NUMW
GROUP BY CATEGORY;

--- 9.	Which producers in the Sousse region have harvested at least one wine in quantities greater than 300 liters? We want the names and first names of the producers, sorted in alphabetical order.
SELECT DISTINCT PRODUCER.FIRSTNAME, PRODUCER.LASTNAME
FROM PRODUCER
JOIN HARVEST ON PRODUCER.NUMP = HARVEST.NUMP
WHERE REGION = 'SOUSSE'
  AND HARVEST.QUANTITY > 300
ORDER BY PRODUCER.FIRSTNAME, PRODUCER.LASTNAME;

--- 10.	List the wine numbers that have a degree greater than 12 and that have been produced by producer number 24.
SELECT NUMW
FROM WINE
WHERE degree > 12;
  


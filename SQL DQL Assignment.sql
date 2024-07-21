

-- ### Practice Questions for Data Query Language (DQL) Statements ###

-- 1. Retrieve all authors.
SELECT * FROM AUTHORS;

-- 2. Retrieve the names and email addresses of all customers.
SELECT NAME, EMAIL FROM CUSTOMERS;

-- 3. List all books along with their authors' names.
SELECT BOOKS.TITLE, AUTHORS.AUTHOR_NAME FROM BOOKS
JOIN AUTHORS ON BOOKS.BOOK_ID=AUTHORS.AUTHOR_ID;

-- 4. Find all books published before the year 2000.
SELECT BOOK_ID, TITLE, PUBLICATION_YEAR FROM BOOKS
WHERE PUBLICATION_YEAR <= 2000;

-- 5. Get the total number of books written by British authors.
SELECT COUNT(*) AS NUMBEROFBOOKS, AUTHORS.NATIONALITY
FROM BOOKS
JOIN AUTHORS ON BOOKS.AUTHOR_ID = AUTHORS.AUTHOR_ID
WHERE NATIONALITY = 'BRITISH'
GROUP BY NATIONALITY;


-- 6. Retrieve the titles of all books reviewed by 'John Doe'.
SELECT BOOKS.TITLE, CUSTOMERS.NAME, REVIEWS.REVIEW_ID
FROM BOOKS
JOIN CUSTOMERS ON BOOKS.TITLE = CUSTOMERS.NAME 
JOIN REVIEWS ON BOOKS.BOOK_ID = REVIEWS.REVIEW_ID


-- 7. Find the average rating for each book.
SELECT BOOKS.BOOK_ID,  AVG(Rating)
8, AVG(RATING)
FROM REVIEWS 
GROUP BY BOOK_ID;

-- 8. List all orders made in the year 2023.
select * from orders
where ORDER_DATE LIKE '2023%'

-- 9. Retrieve the most recent review for each book.
SELECT b.title AS book_title, r.review_id, r.review_text
FROM (
    SELECT 
        book_id, 
        review_id, 
        review_text,
        ROW_NUMBER() OVER(PARTITION BY book_id ORDER BY review_date DESC) AS rn
    FROM reviews
) r
JOIN books b ON b.book_id = r.book_id
WHERE r.rn = 1;

-- 10. Find all customers who have never placed an order.
SELECT Customers.Customer_ID, Customers.NAME
FROM Customers
JOIN Orders ON Customers.Customer_ID = Orders.Customer_ID
WHERE Orders.Customer_ID = 0;

-- 11. List the top 5 highest-rated books based on average ratings.
SELECT BOOKS.BOOK_ID, BOOKS.Title, AVG(Rating) AS AvgRating
FROM Books 
JOIN Reviews ON BOOKS.Book_ID = REVIEWS.BOOK_ID
GROUP BY books.Book_ID, books.Title
ORDER BY AVGRATING DESC
LIMIT -5;

-- 12. Retrieve the details of all American authors.
SELECT AUTHOR_ID, AUTHOR_NAME, NATIONALITY 
FROM AUTHORS 
WHERE NATIONALITY = 'AMERICAN';

-- 13. Find the total number of orders placed by each customer.
SELECT COUNT(*) AS NUMBEROFORDERS, CUSTOMER_ID
FROM ORDERS
GROUP BY CUSTOMER_ID;

-- 14. List the titles of all books and their corresponding review texts.
SELECT BOOKS.TITLE, REVIEWS.REVIEW_TEXT 
FROM BOOKS
JOIN REVIEWS ON REVIEWS.BOOK_ID = BOOKS.BOOK_ID;

-- 15. Retrieve the names of all authors who have written more than one book.
SELECT * FROM BOOKS;
SELECT AUTHORS.AUTHOR_NAME
FROM AUTHORS 
JOIN BOOKS ON AUTHORS.AUTHOR_ID = BOOKS.AUTHOR_ID
GROUP BY AUTHORS.AUTHOR_NAME
HAVING COUNT (BOOKS.book_id) > 1;

-- 16. Retrieve all books with the word 'the' in the title (case-insensitive).
SELECT TITLE FROM BOOKS
WHERE TITLE LIKE '%THE%';

-- 17. Find all customers whose email addresses end with 'example.com'.
SELECT CUSTOMER_ID, NAME FROM CUSTOMERS
WHERE EMAIL LIKE '%example.com%';

-- 18. Retrieve the names and birthdates of customers born in the 1980s.
SELECT NAME, BIRTH_DATE FROM CUSTOMERS
WHERE BIRTH_DATE >= 1980/1/1;
SELECT * FROM CUSTOMERS

-- 19. List all authors from either the 'British' or 'American' nationality using a set operator.
SELECT AUTHOR_ID, AUTHOR_NAME, NATIONALITY 
FROM AUTHORS 
WHERE NATIONALITY IN ('AMERICAN', 'BRITISH');

-- 20. Retrieve the titles and publication years of books published after 2000 but not in 2023 using a set operator.
SELECT title, publication_year
FROM books
WHERE publication_year > 2000
  AND publication_year <> 2023;

-- 21. Find all books whose titles start with 'The'.
SELECT TITLE FROM BOOKS
WHERE TITLE LIKE 'THE';

-- 22. Retrieve the titles of books and their genres where the genre contains 'Fiction'.
SELECT title, genre
FROM books
WHERE genre LIKE '%Fiction%';

-- 23. List the names of customers who have either 'John' or 'Jane' in their name.
SELECT NAME FROM CUSTOMERS
WHERE NAME LIKE '%JOHN%' 
OR NAME LIKE '%JANE%';

-- 24. Find all authors whose names end with 'ing'.
SELECT AUTHOR_NAME FROM AUTHORS
WHERE AUTHOR_NAME LIKE '%ING%'

-- 25. Retrieve the names and nationalities of authors where the name contains exactly five letters.
SELECT AUTHOR_NAME, NATIONALITY FROM AUTHORS
WHERE AUTHOR_NAME LENGTH = 5;
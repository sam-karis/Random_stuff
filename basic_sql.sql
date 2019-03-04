--Basic select query 
SELECT 'Hello', 'World';

--Basic select query with alias
SELECT 'Hello' as FirstWord, 'World' as SecondWord;

--Query column without table qualifying
SELECT full_name, email, username
FROM user_user;

--Query qualifying column name
SELECT user_user.full_name, user_user.email, user_user.username
FROM user_user;

--Query qualifying column name with table alias(Best Practice)
SELECT u.full_name, u.email, u.username
FROM user_user u;

-- DISTINCT value
SELECT DISTINCT u.full_name
FROM user_user u;

-- Where clause with equals oparator
SELECT u.full_name, u.email, u.username
FROM user_user u
WHERE u.username = 'samkaris';

-- Where clause with not equals oparator
SELECT u.full_name, u.email, u.username
FROM user_user u
WHERE u.username <> 'samkaris';

-- Where clause with AND clause
SELECT u.full_name, u.email, u.username
FROM user_user u
WHERE u.username = 'samkaris' AND u.full_name = 'sammy Kariuki';

-- Where clause with OR clause
SELECT u.full_name, u.email, u.username
FROM user_user u
WHERE u.username = 'samkaris1' OR u.email = 'samkaris@gmail.com';

-- Between Oparator
SELECT u.username
FROM user_user u
WHERE u.id BETWEEN 4 AND 7;

-- Like Oparator
SELECT u.username, u.full_name, u.email
FROM user_user u
WHERE u.username LIKE '%karis1%';

-- IN Oparator
SELECT u.id, u.username, u.email
FROM user_user u
WHERE u.id IN (1, 3, 6);

-- IS and IS NOT Oparator are always accompanied by NULL
SELECT u.username, u.full_name, u.email
FROM user_user u
WHERE u.last_login IS NULL;

SELECT u.username, u.full_name, u.email
FROM user_user u
WHERE u.last_login IS NOT NULL;


-- Shaping Results

-- ORDER_BY clause
SELECT u.username, u.full_name, u.email
FROM user_user u
ORDER BY u.email;
SELECT u.username, u.full_name, u.email
FROM user_user u
ORDER BY u.email DESC;

-- SET functions(COUNT, MAX, MIN, AVG, SUM)
-- COUNT
SELECT COUNT(*)
FROM user_user u
WHERE u.full_name LIKE 'sam%';
-- MAX, MIN, AVG, SUM
SELECT MAX(u.id), MIN(u.id), AVG(u.id), SUM(u.id)
FROM user_user u;

--SET funtions and Qualifiers
SELECT COUNT(DISTINCT u.full_name)
FROM user_user u
WHERE u.full_name LIKE 'sam%';

-- GROUP BY Clause
SELECT COUNT(u.full_name), u.full_name
FROM user_user u
GROUP BY u.full_name
;
SELECT COUNT(DISTINCT u.full_name), u.full_name
FROM user_user u
GROUP BY u.full_name
;

-- HAVING
SELECT COUNT(u.full_name), u.full_name
FROM user_user u
GROUP BY u.full_name
HAVING COUNT(u.full_name) > 1;
-- Use alias
SELECT COUNT(u.full_name) as FullNameCount, u.full_name
FROM user_user u
GROUP BY u.full_name
HAVING COUNT(u.full_name) > 1
;



-- JOIN clause
--CROSS JOIN - Bad Practice
SELECT u.username, p.bio
FROM user_user u, user_profile p;

-- INNER JOIN - Most typical - Ignores null rows
SELECT u.username, p.bio
FROM user_user u INNER JOIN user_profile p ON u.id = p.user_id;

--OUTER JOIN(LEFT/RIGHT/FULL) - Take into account null values
-- LEFT OUTER JOIN - All rows from left are included
SELECT u.username, p.bio
FROM user_user u LEFT OUTER JOIN user_profile p ON u.id = p.user_id;
-- RIGHT OUTER JOIN - All rows from right are included
SELECT u.username, p.company
FROM user_user u RIGHT OUTER JOIN user_profile p ON u.id = p.user_id;
-- FULL OUTER JOIN - All rows from all tables are included
SELECT u.username, p.company
FROM user_user u FULL OUTER JOIN user_profile p ON u.id = p.user_id;
-- SELF JOIN - No special syntax for is used to join table by itself and it can apply all other joins



-- INSERT CLAUSE
INSERT INTO user_profile
    (bio, company, phone, updated_at)
VALUES
    ('Analyst', 'Andela', '2547..', '2019-03-03 19:51:59.272497+03');

-- BULK INSERT using select Clause
INSERT INTO person
p
SELECT *
FROM old_person
WHERE op.id > 1000;
-- BULK INSERT using list of values
INSERT INTO
user_profile
    (bio, company, phone, updated_at, user_id)
VALUES
    ('Analyst', 'Google', '2547..', '2019-03-03 19:51:59.272497+03', 1),
    ('Developer', 'Andela', '2547..', '2019-03-03 19:51:59.272497+03', 3);


-- UPDATE CLAUSE
UPDATE user_user u
SET username
= 'samkaris' WHERE u.id = 1;

-- DELETE CLAUSE
DELETE FROM user_user u WHERE u.id = 10;



-- Creating Database tables(DATA DEFINITION LANGUAGE- DDL)
CREATE DATABASE contacts;

USE DATABASE contacts;

SELECT *
FROM person p;
--ALternatively qualify the table name full instead of using USE

-- CREATE TABLE
CREATE TABLE person
(
    id INTEGER PRIMARY KEY,
    person_name CHARACTER,
    email VARCHAR(55)
);

-- ALTER TABLE
ALTER TABLE emails ADD CONSTRAINT fk_email_address FOREIGN KEY (email_address_person_id) REFERENCES person (person_id);


-- DROP TABLE
DROP TABLE person;





-- 1. Find duplicate records in a table
SELECT customer_id, count(*) as order_count FROM Orders
GROUP BY customer_id
HAVING count(*)>1;

SELECT c.customer_id, c.first_name, count(*) as order_count
FROM Customers as c
JOIN Orders as o
ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.first_name
HAVING count(*)>1;


-- 2. Retrieve second highest salary
SELECT name, salary
FROM Employee
ORDER By Salary DESC LIMIT 1 OFFSET 1; --use only if no duplicates

SELECT MAX(salary) as max_salary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);

-- If interviewer asks for employee name too, then:

SELECT name, salary
FROM Employee
WHERE salary = (
    SELECT MAX(salary)
    FROM Employee
    WHERE salary < (SELECT MAX(salary) FROM Employee)
);


-- 3. Count orders per customer
SELECT customer_id, Count(*) as order_count
FROM Orders
GROUP BY customer_id;

SELECT c.customer_id, c.first_name, Count(*) as order_count
FROM Customers as c
JOIN Orders as o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name; -- if selecting name add that too in group by


-- 4. Retrieve employees who joined in 2023
SELECT name FROM Employee
WHERE hire_date between '2023-01-01' AND '2023-12-31';
-- or WHERE hire_date >= '2023-01-01' AND hire_date < '2024-01-01'
-- or WHERE EXTRACT(YEAR FROM hire_date) = 2023;


-- 5. Calculate total revenue per product
SELECT product_id, SUM(quantity*price) as total_revenue
FROM Sales
GROUP BY product_id;
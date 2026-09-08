SQL INTERVIEW FUNDAMENTALS — REVISION QUESTION BANK

Priority:
P0 = must know
P1 = important
P2 = deeper/follow-up

Hide the answers and write queries from a blank editor.
Always consider NULLs, duplicates, ties, indexes, and query plans.

-- ============================================================
-- BASIC SELECT / FILTERING
-- ============================================================

-- Q1 [P0] Select employees with salary > 100000.
SELECT *
FROM employee
WHERE salary > 100000;

-- Q2 [P0] WHERE vs HAVING?
-- ANSWER:
-- WHERE filters rows before grouping/aggregation.
-- HAVING filters groups after GROUP BY/aggregation.

-- Q3 [P0] What does DISTINCT do?
-- ANSWER: Removes duplicate rows from the selected result.

-- Q4 [P0] NULL vs 0?
-- ANSWER: NULL means missing/unknown; 0 is an actual numeric value.

-- Q5 [P0] Why is column = NULL incorrect?
-- ANSWER: Use IS NULL / IS NOT NULL.

-- ============================================================
-- ORDERING / PAGINATION
-- ============================================================

-- Q6 [P0] Find 5 highest salaries.
SELECT salary
FROM employee
ORDER BY salary DESC
LIMIT 5;

-- Q7 [P0] What does OFFSET 5 do?
-- ANSWER: Skips the first 5 rows of the ordered result.

-- Q8 [P1] Why can large OFFSET pagination become slow?
-- ANSWER: The database may still scan/skip many rows.
-- Keyset/cursor pagination can scale better for large offsets.

-- ============================================================
-- AGGREGATIONS
-- ============================================================

-- Q9 [P0] Highest salary.
SELECT MAX(salary) FROM employee;

-- Q10 [P0] Average salary.
SELECT AVG(salary) FROM employee;

-- Q11 [P0] Count employees.
SELECT COUNT(*) FROM employee;

-- Q12 [P0] COUNT(*) vs COUNT(column)?
-- ANSWER:
-- COUNT(*) counts rows.
-- COUNT(column) counts non-NULL values.

-- Q13 [P0] Employees per department.
SELECT department_id, COUNT(*)
FROM employee
GROUP BY department_id;

-- Q14 [P0] Departments with more than 10 employees.
SELECT department_id, COUNT(*)
FROM employee
GROUP BY department_id
HAVING COUNT(*) > 10;

-- ============================================================
-- JOINS
-- ============================================================

-- Q15 [P0] What is INNER JOIN?
-- ANSWER: Returns rows where the join condition matches in both tables.

-- Q16 [P0] What is LEFT JOIN?
-- ANSWER: Keeps all left-table rows and matching right-table rows.
-- Unmatched right columns become NULL.

-- Q17 [P0] Employee names and department names.
SELECT e.name, d.name AS department_name
FROM employee e
JOIN department d ON e.department_id = d.id;

-- Q18 [P0] Employees with no matching department.
SELECT e.*
FROM employee e
LEFT JOIN department d ON e.department_id = d.id
WHERE d.id IS NULL;

-- Q19 [P1] INNER JOIN vs LEFT JOIN?
-- ANSWER: INNER keeps only matches; LEFT keeps every left-side row.

-- Q20 [P1] What is a self join?
-- ANSWER: Joining a table to itself, often for hierarchical relationships.

-- ============================================================
-- SUBQUERIES
-- ============================================================

-- Q21 [P0] Second-highest DISTINCT salary.
SELECT MAX(salary)
FROM employee
WHERE salary < (
    SELECT MAX(salary)
    FROM employee
);

-- Q22 [P0] Why doesn't SELECT MAX(salary) answer second-highest salary?
-- ANSWER: It returns the highest salary; the highest must first be excluded.

-- Q23 [P1] Employees earning above company average.
SELECT *
FROM employee
WHERE salary > (
    SELECT AVG(salary)
    FROM employee
);

-- Q24 [P1] What is a correlated subquery?
-- ANSWER: A subquery that references columns from the outer query.

-- ============================================================
-- WINDOW FUNCTIONS
-- ============================================================

-- Q25 [P0] Second-highest DISTINCT salary using DENSE_RANK.
SELECT salary
FROM (
    SELECT salary,
           DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM employee
) t
WHERE salary_rank = 2;

-- Q26 [P0] ROW_NUMBER vs RANK vs DENSE_RANK?
-- ANSWER:
-- ROW_NUMBER: unique sequential numbers.
-- RANK: ties share rank and gaps appear.
-- DENSE_RANK: ties share rank and no gaps.
--
-- For 100,100,90,80:
-- ROW_NUMBER: 1,2,3,4
-- RANK:       1,1,3,4
-- DENSE_RANK: 1,1,2,3

-- Q27 [P0] Highest-paid employee in each department.
SELECT *
FROM (
    SELECT e.*,
           ROW_NUMBER() OVER (
               PARTITION BY department_id
               ORDER BY salary DESC
           ) AS rn
    FROM employee e
) t
WHERE rn = 1;

-- Q28 [P1] Top 3 salaries in each department.
SELECT *
FROM (
    SELECT e.*,
           DENSE_RANK() OVER (
               PARTITION BY department_id
               ORDER BY salary DESC
           ) AS rnk
    FROM employee e
) t
WHERE rnk <= 3;

-- Q29 [P1] What does PARTITION BY do?
-- ANSWER: Creates independent groups for a window calculation without
-- collapsing rows like GROUP BY.

-- ============================================================
-- COMMON INTERVIEW QUERIES
-- ============================================================

-- Q30 [P0] Find duplicate emails.
SELECT email, COUNT(*)
FROM users
GROUP BY email
HAVING COUNT(*) > 1;

-- Q31 [P0] Latest record for each user.
SELECT *
FROM (
    SELECT t.*,
           ROW_NUMBER() OVER (
               PARTITION BY user_id
               ORDER BY created_at DESC
           ) AS rn
    FROM transactions t
) x
WHERE rn = 1;

-- Q32 [P1] Users who never placed an order.
SELECT u.*
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
WHERE o.id IS NULL;

-- Q33 [P1] Records created in the last 7 days.
SELECT *
FROM events
WHERE created_at >= CURRENT_TIMESTAMP - INTERVAL '7 days';

-- Q34 [P1] Employees earning above their department average.
SELECT *
FROM employee e
WHERE salary > (
    SELECT AVG(e2.salary)
    FROM employee e2
    WHERE e2.department_id = e.department_id
);

-- ============================================================
-- EXISTS / IN
-- ============================================================

-- Q35 [P0] What does EXISTS do?
-- ANSWER: Tests whether a subquery returns at least one row.

-- Q36 [P0] Users with at least one order.
SELECT u.*
FROM users u
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.user_id = u.id
);

-- Q37 [P1] EXISTS vs IN?
-- ANSWER: Both express membership/existence, but NULL semantics and
-- query plans can differ. Do not claim one is always faster.

-- ============================================================
-- NULL / COALESCE / CASE
-- ============================================================

-- Q38 [P0] What does COALESCE do?
-- ANSWER: Returns the first non-NULL expression.
SELECT COALESCE(phone, 'Not provided')
FROM users;

-- Q39 [P0] Salary bands.
SELECT name,
       CASE
           WHEN salary >= 100000 THEN 'HIGH'
           WHEN salary >= 50000 THEN 'MEDIUM'
           ELSE 'LOW'
       END AS salary_band
FROM employee;

-- Q40 [P1] Why can NOT IN behave unexpectedly with NULLs?
-- ANSWER: SQL uses three-valued logic. NULL can make comparisons UNKNOWN.
-- NOT EXISTS is often safer when NULL semantics matter.

-- ============================================================
-- INDEXES
-- ============================================================

-- Q41 [P0] Create an email index.
CREATE INDEX idx_users_email
ON users(email);

-- Q42 [P0] Why can an index improve reads?
-- ANSWER: It can provide an efficient access path to matching rows.

-- Q43 [P0] Index trade-offs?
-- ANSWER: Extra storage and additional work for writes/index maintenance.

-- Q44 [P0] Should every column be indexed?
-- ANSWER: No. Index based on actual workload and query patterns.

-- Q45 [P1] Composite index.
CREATE INDEX idx_orders_user_status
ON orders(user_id, status);

-- Q46 [P1] Why does composite-index column order matter?
-- ANSWER: B-tree indexes are ordered by leading columns; query patterns
-- involving those leading columns generally benefit most directly.

-- ============================================================
-- EXPLAIN / PERFORMANCE
-- ============================================================

-- Q47 [P0] What is EXPLAIN?
-- ANSWER: Shows the planned query execution strategy.
EXPLAIN
SELECT *
FROM users
WHERE email = 'a@example.com';

-- Q48 [P0] What is EXPLAIN ANALYZE?
-- ANSWER: Executes the query and reports actual execution statistics.

-- Q49 [P1] What is a sequential scan?
-- ANSWER: PostgreSQL scans table data sequentially rather than using an
-- index access path.

-- Q50 [P1] When can a sequential scan be better?
-- ANSWER: When a large portion of the table is needed, sequential access
-- can be cheaper than many index-driven/random accesses.

-- ============================================================
-- TRANSACTIONS / ACID
-- ============================================================

-- Q51 [P0] What is a transaction?
-- ANSWER: A logical unit of work with commit/rollback semantics.

-- Q52 [P0] What does COMMIT do?
-- ANSWER: Commits the transaction's changes.

-- Q53 [P0] What does ROLLBACK do?
-- ANSWER: Reverts uncommitted changes in the transaction.

-- Q54 [P0] What are ACID properties?
-- ANSWER: Atomicity, Consistency, Isolation, Durability.

-- ============================================================
-- CONCURRENCY / ISOLATION
-- ============================================================

-- Q55 [P1] Dirty read?
-- ANSWER: Reading uncommitted data from another transaction.

-- Q56 [P1] Non-repeatable read?
-- ANSWER: Re-reading a row and seeing a different committed value because
-- another transaction changed it.

-- Q57 [P1] Phantom read?
-- ANSWER: Repeating a query and seeing a different set of matching rows
-- due to concurrent inserts/deletes.

-- ============================================================
-- CONSTRAINTS
-- ============================================================

-- Q58 [P0] Primary key?
-- ANSWER: Uniquely identifies rows and cannot be NULL.

-- Q59 [P0] Foreign key?
-- ANSWER: Enforces a relationship to a key in another table.

-- Q60 [P0] UNIQUE vs PRIMARY KEY?
-- ANSWER: PRIMARY KEY identifies the row and is NOT NULL; UNIQUE enforces
-- uniqueness but is not the table's primary identifier.

-- Q61 [P1] CHECK constraint?
-- ANSWER: Requires a Boolean condition to hold.

-- Q62 [P1] Why enforce integrity at the database level?
-- ANSWER: It provides a final consistency boundary even when multiple
-- applications/services write to the same data.

-- ============================================================
-- DELETE / TRUNCATE / DROP
-- ============================================================

-- Q63 [P0] DELETE vs TRUNCATE vs DROP?
-- ANSWER:
-- DELETE removes rows and supports WHERE.
-- TRUNCATE removes all rows efficiently.
-- DROP removes the table/object.

-- Q64 [P1] When use DELETE rather than TRUNCATE?
-- ANSWER: When deleting selected rows or when row-level behavior and
-- transaction/constraint semantics make DELETE appropriate.

-- ============================================================
-- CTE / VIEWS
-- ============================================================

-- Q65 [P1] What is a CTE?
-- ANSWER: A named subquery defined with WITH, useful for readable,
-- composable queries and recursive queries.

WITH high_paid AS (
    SELECT *
    FROM employee
    WHERE salary > 100000
)
SELECT *
FROM high_paid;

-- Q66 [P2] What is a recursive CTE?
-- ANSWER: A CTE that refers to itself, useful for hierarchical data.

-- Q67 [P1] What is a view?
-- ANSWER: A stored query that behaves like a virtual table.

-- Q68 [P2] What is a materialized view?
-- ANSWER: A stored query result that can be refreshed, trading freshness
-- for potentially faster reads.

-- ============================================================
-- NORMALIZATION
-- ============================================================

-- Q69 [P1] What is normalization?
-- ANSWER: Structuring relational data to reduce redundancy and anomalies.

-- Q70 [P1] What is denormalization?
-- ANSWER: Intentionally adding redundancy for performance/simplicity,
-- accepting consistency/storage trade-offs.

-- ============================================================
-- BACKEND SQL
-- ============================================================

-- Q71 [P0] Latest status for every order.
SELECT *
FROM (
    SELECT os.*,
           ROW_NUMBER() OVER (
               PARTITION BY order_id
               ORDER BY created_at DESC
           ) AS rn
    FROM order_status os
) x
WHERE rn = 1;

-- Q72 [P0] Users with >3 failed login attempts.
SELECT user_id, COUNT(*) AS failed_attempts
FROM login_attempts
WHERE status = 'FAILED'
GROUP BY user_id
HAVING COUNT(*) > 3;

-- Q73 [P1] Top 5 users by order count.
SELECT user_id, COUNT(*) AS order_count
FROM orders
GROUP BY user_id
ORDER BY order_count DESC
LIMIT 5;

-- Q74 [P1] Users with orders but no successful payment.
-- ANSWER:
-- Clarify the schema and meaning first. One approach is NOT EXISTS:
SELECT u.*
FROM users u
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.user_id = u.id
)
AND NOT EXISTS (
    SELECT 1
    FROM payments p
    JOIN orders o ON o.id = p.order_id
    WHERE o.user_id = u.id
      AND p.status = 'SUCCESS'
);

-- ============================================================
-- RAPID FIRE
-- ============================================================
-- Q75 WHERE vs HAVING?
-- Q76 INNER JOIN vs LEFT JOIN?
-- Q77 COUNT(*) vs COUNT(column)?
-- Q78 NULL vs 0?
-- Q79 DELETE vs TRUNCATE?
-- Q80 PRIMARY KEY vs UNIQUE?
-- Q81 What is an index?
-- Q82 Why do indexes have write cost?
-- Q83 What is a composite index?
-- Q84 What is a transaction?
-- Q85 What are ACID properties?
-- Q86 Second-highest DISTINCT salary?
-- Q87 Duplicate rows?
-- Q88 Latest row per user?
-- Q89 Top N per group?
-- Q90 ROW_NUMBER vs RANK vs DENSE_RANK?
-- Q91 EXISTS vs IN?
-- Q92 What is a CTE?
-- Q93 What does EXPLAIN show?
-- Q94 What does EXPLAIN ANALYZE do?
-- Q95 When can sequential scan be better?

-- REVISION RULE:
-- Do not memorize queries only.
-- For every query ask:
-- 1. What rows exist before this clause?
-- 2. What does this clause do?
-- 3. What happens with NULL?
-- 4. What happens with duplicates/ties?
-- 5. Could an index help?
-- 6. What might EXPLAIN show?

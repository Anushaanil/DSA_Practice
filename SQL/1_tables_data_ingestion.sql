CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    age INT,
    country VARCHAR(100)
);

CREATE TABLE Department (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

CREATE TABLE Employee (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT,
    department_id INT,
    hire_date DATE,
    FOREIGN KEY (department_id) REFERENCES Department(department_id)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    item VARCHAR(100),
    amount INT,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Sales (
    product_id INT,
    quantity INT,
    price INT
);

CREATE TABLE Shippings (
    shipping_id INT PRIMARY KEY,
    status VARCHAR(50),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE INDEX idx_orders_customer ON Orders(customer_id);
CREATE INDEX idx_employee_department ON Employee(department_id);

INSERT INTO Customers VALUES
(1, 'John', 'Doe', 31, 'USA'),
(2, 'Robert', 'Luna', 22, 'USA'),
(3, 'David', 'Robinson', 22, 'UK'),
(4, 'John', 'Reinhardt', 25, 'UK'),
(5, 'Betty', 'Doe', 28, 'UAE'),
(6, 'Alice', 'Smith', 30, 'India'); -- no orders (important edge case)

INSERT INTO Department VALUES
(1, 'HR'),
(2, 'Engineering'),
(3, 'Sales');


INSERT INTO Employee VALUES
(1, 'A', 50000, 1, '2023-01-10'),
(2, 'B', 70000, 1, '2022-03-15'),
(3, 'C', 60000, 2, '2023-07-20'),
(4, 'D', 90000, 2, '2021-11-05'),
(5, 'E', 40000, NULL, '2023-05-01'), -- no department
(6, 'F', 90000, 2, '2022-06-01'); -- tie salary

INSERT INTO Orders VALUES
(1, 'Keyboard', 400, 4),
(2, 'Mouse', 300, 4),
(3, 'Monitor', 12000, 3),
(4, 'Keyboard', 400, 1),
(5, 'Mousepad', 250, 2),
(6, 'Keyboard', 400, 1), -- duplicate-style scenario
(7, 'Laptop', 50000, 3);

INSERT INTO Sales VALUES
(1, 2, 100),
(2, 1, 200),
(1, 3, 100), -- duplicate product_id
(3, 5, 50),
(4, 0, 500); -- zero quantity edge case

INSERT INTO Shippings VALUES
(1, 'Pending', 2),
(2, 'Pending', 4),
(3, 'Delivered', 3),
(4, 'Pending', 5),
(5, 'Delivered', 1);
--  (6, 'Pending', 7); invalid FK (to test thinking)


-- Exercise src/dataframe_api/exercise2 done in MySQL
/*
Compute each employee’s current salary from salaries (filter to_date='9999-01-01').
Map each employee to their current department from dept_emp (same to_date filter).
Compute the average current salary per department.
Return the top 3 departments by that average, also include the employee count used in the average.
*/
USE EMPLOYEES
DROP VIEW IF EXISTS exercise_2;

CREATE VIEW exercise_2 AS
SELECT
  e.emp_no,
  e.first_name,
  e.last_name,
  s.salary
FROM
  employees e
  INNER JOIN salaries s ON e.emp_no = s.emp_no
WHERE
  s.to_date = '9999-01-01'
LIMIT
  20;

SELECT
  *
FROM
  exercise_2;

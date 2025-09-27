-- Exercise src/dataframe_api/exercise2 done in MySQL
/*
Compute each employee’s current salary from salaries (filter to_date='9999-01-01').
Map each employee to their current department from dept_emp (same to_date filter).
Compute the average current salary per department.
Return the top 3 departments by that average, also include the employee count used in the average.
*/
USE Employees
SELECT
  e.emp_no,
  e.first_name,
  e.last_name,
  d.dept_no,
  dn.dept_name
FROM
  employees e
  INNER JOIN dept_emp d ON e.emp_no = d.emp_no
  INNER JOIN departments dn ON d.dept_no = dn.dept_no
WHERE
  d.to_date = "9999-01-01"
LIMIT
  20;

/*
Using the standard employees dataset (tables: employees, salaries, dept_emp, departments), return the top 3 departments by average current salary among current employees only.
Requirements:
“Current” = records with to_date = '9999-01-01' in both salaries and dept_emp.
Only include departments with at least 50 current employees.
Output columns: dept_no, dept_name, employee_count, avg_salary (round to nearest integer).
Sort by avg_salary desc, then dept_no asc for ties.
Aim for one SQL statement.
*/
USE Employees;

SELECT
  d.dept_name,
  COUNT(*) AS nr_of_emp,
  ROUND(AVG(s.salary)) avg_salary
FROM
  departments d
  INNER JOIN dept_emp de ON de.dept_no = d.dept_no
  AND de.to_date = "9999-01-01"
  INNER JOIN salaries s ON s.emp_no = de.emp_no
  AND s.to_date = "9999-01-01"
GROUP BY
  d.dept_no,
  d.dept_name
HAVING
  COUNT(*) >= 50
ORDER BY
  avg_salary DESC,
  d.dept_no ASC
LIMIT
  3;

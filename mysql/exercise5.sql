/* 
Q1. Current headcount & avg salary per department (simple)
Return one row per department with: dept_no, dept_name, employee_count, avg_salary_current.
Rules: only current employees (dept_emp.to_date='9999-01-01') and current salaries (salaries.to_date='9999-01-01'). Order by employee_count desc, then dept_no.
(Expect a straightforward 2-join aggregation.)
*/
USE Employees;

SELECT
  de.dept_no,
  d.dept_name,
  COUNT(*) as employee_count,
  ROUND(AVG(s.salary)) avg_salary
FROM
  dept_emp de
  INNER JOIN salaries s ON de.emp_no = s.emp_no
  AND s.to_date = "9999-01-01"
  INNER JOIN departments d ON d.dept_no = de.dept_no
WHERE
  de.to_date = "9999-01-01"
GROUP BY
  de.dept_no,
ORDER BY
  employee_count DESC,
  dept_no ASC;

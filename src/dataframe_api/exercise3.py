"""
Map each employee to their current department from dept_emp (same to_date filter).
"""

from dataframe_objs import departments_df, dept_emp_df, employees_df
from pyspark.sql import functions as F

# Exercise 3: condition above - (PySpark)
# Staging - ensuring that the to_date has the type 'date'
dept_emp_df_stg = dept_emp_df.withColumn("to_date", F.to_date("to_date"))

# dept_emp_df_current will hold only the departments that are still working
dept_emp_df_current = dept_emp_df.filter(
    F.col("to_date") == F.to_date(F.lit("9999-01-01"))
)

# Inner join with employees to get the right employees for each department
employees_df_dept = employees_df.join(
    dept_emp_df_current,
    on="emp_no",
    how="inner",
)

# Inner join with departments to get the department name as well
departments = employees_df_dept.join(departments_df, on="dept_no", how="inner")

result = departments.select("first_name", "last_name", "dept_name")
result.show(20)

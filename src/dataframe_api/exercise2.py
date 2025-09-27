"""
Compute each employee’s current salary from salaries (filter to_date='9999-01-01').
"""

# Dataframe_objs/ can be found in dataframe_api/
from dataframe_objs import employees_df, salaries_df, spark
from pyspark.sql import functions as F

# Exercise 2: condition above (PySpark)
salaries_std = salaries_df.withColumn("to_date", F.to_date("to_date"))
current_salaries = salaries_std.filter(
    F.col("to_date") == F.to_date(F.lit("9999-01-01"))
)

emp_with_salaries = employees_df.join(current_salaries, on="emp_no", how="inner")

result = emp_with_salaries.select("emp_no", "first_name", "last_name", "salary")

result.show(20)

# Exercise 2: condition above (Spark)
# Register the DataFrames as views since spark object below needs them
employees_df.createOrReplaceTempView("employees")
salaries_df.createOrReplaceTempView("salaries")

emp_with_salaries = spark.sql(
    """
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
"""
)
emp_with_salaries.show()

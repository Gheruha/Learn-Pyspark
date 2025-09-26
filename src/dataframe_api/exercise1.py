"""
Goal: From employees table, build a cleaned view of people hired since 2000-01-01, compute their tenure, bucket them into bands, and list the 10 most recent hires.
"""

# Dataframe_objs/ can be found in dataframe_api/
from dataframe_objs import employees_df
from pyspark.sql import functions as F

# Exercise 1_1: Making a view of people hired since 2000-01-01

# Making a copy(staging) of employees dataframe, ensuring that all the dates are of 'date' datatype
employees_stg = employees_df.withColumn("hire_date", F.to_date("hire_date"))

# Making a view with the empoloyees hired since 2000-01-01
recent_employees = employees_stg.filter(
    F.col("hire_date") >= F.to_date(F.lit("2000-01-01"))
)

recent_employees.show()

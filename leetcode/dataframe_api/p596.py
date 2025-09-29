# EASY LEETCODE: 596. Classes with at least 5 students.
# Spark & Pyspark

from dataframe_objs import leet_596_courses_df, spark
from pyspark.sql import functions as F

leet_596_courses_df.createOrReplaceTempView("Courses")
result_spark = spark.sql(
    """SELECT class 
    FROM Courses
    GROUP BY class
    HAVING COUNT(DISTINCT(student)) >= 5"""
)
result_spark.show()


result_pyspark = (
    leet_596_courses_df.groupBy("class")
    .count()
    .where(F.col("count") >= 5)
    .select("class")
)

result_pyspark.show()

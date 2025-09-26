"""
How to use dataframe_api, using simple exercises:

Requirements:
    1. Database taken from https://github.com/bytebase/employee-sample-database
    2. Connector installed from https://downloads.mysql.com/archives/c-j/
    3. Moved the jar file (only) in ~/drivers/
"""

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("MySQL-Spark")
    .config("spark.jars", "/Users/gheruha/drivers/mysql-connector-j-9.4.0.jar")
    .getOrCreate()
)


df = (
    spark.read.format("jdbc").options(
        url="jdbc:mysql://localhost:3306/employees",
        driver="com.mysql.cj.jdbc.Driver",
        dbtable="employees",
        user="root",
        password="",
    )
).load()

df.show(20)

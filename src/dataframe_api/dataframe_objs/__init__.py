from pyspark.sql import SparkSession

from .config import MYSQL_PROPS, MYSQL_URL

spark = (
    SparkSession.builder.appName("MySQL-Spark")
    .config("spark.jars", "/Users/gheruha/drivers/mysql-connector-j-9.4.0.jar")
    .getOrCreate()
)


def load_table(table_name):
    return spark.read.jdbc(url=MYSQL_URL, table=table_name, properties=MYSQL_PROPS)


# Main tables
employees_df = load_table("employees")
departments_df = load_table("departments")
dept_emp_df = load_table("dept_emp")
dept_manager_df = load_table("dept_manager")
salaries_df = load_table("salaries")
titles_df = load_table("titles")

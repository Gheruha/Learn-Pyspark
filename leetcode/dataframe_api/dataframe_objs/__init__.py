from pyspark.sql import SparkSession

from .config import MYSQL_PROPS, MYSQL_URL

spark = (
    SparkSession.builder.appName("MySQL-Spark")
    .config("spark.jars", "/Users/gheruha/drivers/mysql-connector-j-9.4.0.jar")
    .getOrCreate()
)


def load_table(table_name):
    return spark.read.jdbc(url=MYSQL_URL, table=table_name, properties=MYSQL_PROPS)


leet_596_courses_df = load_table("courses")

"""
How to use dataframe_api, using simple exercises:

Requirements:
    1. Database taken from https://github.com/bytebase/employee-sample-database
    2. Connector installed from https://downloads.mysql.com/archives/c-j/
    3. Moved the jar file (only) in ~/drivers/
"""

# Dataframe_objs/ can be found in dataframe_api/
from dataframe_objs import employees_df

employees_df.show(20)

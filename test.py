from snowflake.snowpark.types import StringType
from snowflake.snowpark.functions import sproc

@sproc(return_type=StringType(), packages=["snowflake-snowpark-python"])
def hello_from_snowpark(session_):
    return "Hello from Snowpark!"

# Call immediately like in test1.py
hello_from_snowpark()
from snowflake.snowpark.session import Session
from snowflake.snowpark.types import StringType
from snowflake.snowpark.functions import sproc

from snowflake.snowpark.types import IntegerType

@sproc(return_type=IntegerType(), input_types=[IntegerType(), IntegerType()], packages=["snowflake-snowpark-python"])
def add_sp(session_, x, y):
   return session_.sql(f"SELECT {x} + {y}").collect()[0][0]


add_sp(1, 1)
from snowflake.snowpark.session import Session
from snowflake.snowpark.types import StringType
from snowflake.snowpark.functions import sproc


@sproc(
    name="hello_from_snowpark",
    return_type=StringType(),
    input_types=[],  
    replace=True,
    packages=["snowflake-snowpark-python"]
)
def hello_from_snowpark(session):
    return "Hello from Snowpark!"
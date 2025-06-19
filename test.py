from snowflake.snowpark.types import StringType
from snowflake.snowpark.functions import sproc
from snowflake.snowpark.session import Session

@sproc(
    name="hello_from_snowpark",
    return_type=StringType(),
    input_types=[],  # No arguments other than session
    replace=True,
    packages=["snowflake-snowpark-python"]
)
def hello_from_snowpark(session):
    return "Hello from Snowpark!"
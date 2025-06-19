from snowflake.snowpark import Session
from snowflake.snowpark.types import StringType
from snowflake.snowpark.functions import sproc

@sproc(
    session=session,
    name="hello_from_snowpark",
    return_type=StringType(),
    packages=["snowflake-snowpark-python"]
)
# FIX: Remove quotes from type hints
def hello_from_snowpark(session: Session) -> str: 
    return f"Hello from Snowpark!"
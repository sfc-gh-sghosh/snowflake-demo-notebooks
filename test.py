from snowflake.snowpark import Session # Session is imported here
from snowflake.snowpark.types import StringType
from snowflake.snowpark.functions import sproc

@sproc(
    name="hello_from_snowpark",
    return_type=StringType(),
    packages=["snowflake-snowpark-python"]
)
# FIX: Remove quotes from type hints
def hello_from_snowpark(session: Session) -> str: # No quotes around Session, no quotes around str
    return f"Hello from Snowpark!"
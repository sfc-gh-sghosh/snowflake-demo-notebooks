from snowflake.snowpark.session import Session
from snowflake.snowpark.types import StringType
from snowflake.snowpark.functions import sproc

@sproc(
    name="hello_from_snowpark",
    return_type=StringType(),
    replace="true",
    packages=["snowflake-snowpark-python"]
)
# FIX: Remove quotes from type hints
def hello_from_snowpark(session) -> str: 
    return f"Hello from Snowpark!"

result = session.call("hello_from_snowpark")
print(result)
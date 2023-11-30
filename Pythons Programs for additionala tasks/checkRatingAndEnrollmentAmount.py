from sqlalchemy import create_engine
import pandas as pd

# Replace with your actual MySQL database information
DATABASE_URI = "mysql+mysqlconnector://root:@localhost/course_details"

# Create a SQLAlchemy engine to connect to the MySQL database
engine = create_engine(DATABASE_URI)

# Replace 'your_table_name' with the actual table name where your data is stored
table_name = 'course_details'

# Write a SQL query to get courses with rating and students enrolled in descending order
query = f"SELECT course_title, course_rating FROM {table_name} ORDER BY course_rating DESC, CAST(course_students_enrolled AS SIGNED) DESC"

# Execute the query and fetch the results into a pandas DataFrame
df = pd.read_sql_query(query, engine)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Display the result
print(df)

# Dispose of the engine
engine.dispose()

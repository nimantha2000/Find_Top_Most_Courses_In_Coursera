import pandas as pd
from sqlalchemy import create_engine

# Replace with your actual MySQL database information
DATABASE_URI = "mysql+mysqlconnector://root:@localhost/course_details"


# Read the CSV file into a pandas DataFrame
df = pd.read_csv('catalog.csv')

# Create a SQLAlchemy engine to connect to the MySQL database
engine = create_engine(DATABASE_URI)

# Replace 'your_table_name' with the actual table name where you want to insert the data
table_name = 'course_details'

# Insert the data into the MySQL database
df.to_sql(table_name, engine, if_exists='replace', index=False)

# Commit the changes
engine.dispose()

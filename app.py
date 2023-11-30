from flask import Flask, render_template
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)

# Replace with your actual MySQL database information
DATABASE_URI = "mysql+mysqlconnector://root:@localhost/course_details"

# Replace 'course_details' with your actual table name in the database
table_name = 'course_details'

def get_courses(difficulty_level):
    engine = create_engine(DATABASE_URI)

    if difficulty_level == 'All':
        query = f"SELECT * FROM {table_name} LIMIT 50"
    else:
        query = f"SELECT * FROM {table_name} WHERE course_difficulty = '{difficulty_level}' LIMIT 50"

    df = pd.read_sql_query(query, engine)
    engine.dispose()

    return df.to_dict(orient='records')

@app.route('/')
def home():
    courses = get_courses('All')
    return render_template('index.html', courses=courses)

@app.route('/courses/<difficulty_level>')
def display_courses(difficulty_level):
    courses = get_courses(difficulty_level)
    return render_template('index.html', courses=courses, current_tab=difficulty_level)

if __name__ == '__main__':
    app.run(debug=True)

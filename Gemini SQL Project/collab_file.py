# This is the correct code we used to run our project in the google collab notebook.

import sqlite3

# Connect To SQLite Database
connection = sqlite3.connect("student.db")

# Create Cursor Object To Insert Records or Create Table
cursor = connection.cursor()

# Check if the Table Exists and Create if it Doesn't
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    SCORES INT
);
"""
cursor.execute(table_info)

# Insert More Records
cursor.execute("""Insert Into Student values("Brian", "Generative AI", "Models", 100)""")
cursor.execute("""Insert Into Student values("Alia", "Media Marketing", "Influencer", 100)""")
cursor.execute("""Insert Into Student values("Delia", "Work & Travel", "Multitasking", 100)""")
cursor.execute("""Insert Into Student values("Bam Bam", "World Studies", "Leadership", 100)""")
cursor.execute("""Insert Into Student values("Amelia", "Business & Finance", "Corporate Management", 100)""")

# Display ALL Records
print("The inserted records are:")
data = cursor.execute("""SELECT NAME FROM STUDENT""")

for row in data:
    print(row)

# Don't forget to commit the changes and close the connection
connection.commit()
connection.close()


import streamlit as st
import os

import google.generativeai as gemini

## Configure API Key
GOOGLE_API_KEY = "AIzaSyDjPDJCfgA1AwJ8BJBImIopE5hRHh9_o9o"
gemini.configure(api_key = GOOGLE_API_KEY)

## Function To Load Google Gemini Model
def get_gemini_response(question, prompt): 
    model = gemini.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0],question])
    return response.text

## Function To retrieve query from Database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Our Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL Query!
    The SQL Database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION \n\nFor example, \nExample 1 - How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    also the sql query should not have ''' in the beginning or the end of the query
    \nExample 2 - Which Student is focusing on Multitasking?,
    the SQL command will be something like this SELECT * FROM STUDENT 
    where SECTION = "Multitasking";
    also the sql query should not have ''' in the beginning or the end of the query   

    """
]

## Streamlit App
st.set_page_config(page_title = "Para La Casa De Gates")
st.header("Gemini SQL Model")

question = st.text_input("Input: ", key = "input")

submit = st.button("Submit Your Question Here")

## If Submit Is Clicked
if submit:
    response = get_gemini_response(question, prompt)
    response = read_sql_query(response, "student.db")
    st.subheader("The Response Is")
    for row in response:
        print(row)
        st.header(row)

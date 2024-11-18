from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

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


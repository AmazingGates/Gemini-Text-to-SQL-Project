# Now that we have our agenda, we will go into the implementatin of our project.

# Here is a list of implementations we will need to begin.

#   Implementation
#
# 1. SQLlite - Although we can use any SQL, this is the version we will be using. We will be using
#SQL to insert some records by using the Python Programming Language.

# 2. LLM Application - This is the step we will be implementing. We will be using this LLM to create a simple
#UI, where we can specifically write a Query. This LLM Application will communicate with Gemini Pro, and then
#it will communicate with the SQL Database, which will give us the answer we are looking for.

# The next thing we will do is start on our installs.

# We will start by creating a requirements file which will hold all of the installs and packages we will need.

# These are the items that will go into our requirements file.

streamlit
# We will use this to create our frontend.

google-generativeai
# This is how we will be accessing our Gemini Pro model.

python-dotenv
# This package will allow us to access our environment when we use it.

# These are the 3 libraries we will need for this project.

# To install our libraries all at once inside our environment we will run this command
#in our command line ( pip install -r requirements.txt)

# This is a basic step that we will use in every project.

# The next thing we will do is create our .env file.

# This file will hold our google api key.

# Now that that is done, we are done with our requirements.

# Now we'll get back to the implementation.

# The first thing we'll do is take database like SQLlite and insert some record.

# We will do this to show that there are some records to attain, there is a database, so
#that we may query from that particular database.

# For this what we are going to do is create a new file.

# This will be a sqllite.py file.

# In this file we will write the code that will allow us to insert any records into the database.

# The first thing we are going to do is import sqlite3, which is a lite weighted database.

# This is how we will do that 

import sqlite3

# The next thing we will do is connect to SQLlite database.

# This is the code we can use to do that 

connection = sqlite3.connect()

# Inside the connect function we will pass our database name as a parameter.

# We will name our database student.db

connection = sqlite3.connect("student.db")

# So what we're doing here is connecting to this particular database, and if this database does
#not exist then it is going to create this new DB.

# This is our first step.

# The second step is that we will create a cursor object to insert records, or create a table

# This is the code we will use to do that.

cursor = connection.cursor()

# Basically what this means is that this method is responsible for inserting and retreiving records.

# The next thing we want to do is create the table.

# This is how we will write our table information.

# First we have our Query name.

# Inside the query name we will have a STUDENT method that will take as parameter NAME, indicating
#that we want to Name to be the field, and in that field it supports various characters, hence the
#VARCHAR(25).

# This is basically our first column in that particular table.

# The next one we will enter as a parameter is CLASS.

# This CLASS field will also be able to support various characters.

# The third parameter we will pass will be called SECTION.

# This field also supports various characters.

# This is simple, but it it is our entire command.

table_info = """
Create Table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25));
"""

# The next thing we want to do is create this table.

# This is the code we will use to do that

cursor.execute(table_info)

# So as soon as this code gets executed our table will be created with the name STUDENT.

# Next we'll go ahead and insert some records.

## Insert More Records

# This is the code we will use to do that.

cursor.execute("""Insert Into Student values("Brian", "Generative AI", "Models")""")
cursor.execute("""Insert Into Student values("Alia", "Media Marketing", "Influencer")""")
cursor.execute("""Insert Into Student values("Delia", "Work & Travel", "Multitasking")""")
cursor.execute("""Insert Into Student values("Bam Bam", "World Studies", "Leadership")""")
cursor.execute("""Insert Into Student values("Amelia", "Business & Finance", "Corporate Management")""")

# So basically what we are doing here is inserting these values into their respective locations
#in our created table named STUDENT.

# We have inserted values into the NAME field, the CLASS field, and the SECTION field.

# Also notice that we inserted a total of five records.

# Each record has different values of information.

# Now that we have all of our records,, we will display them.

# This is the code we will use to do that.

## Display ALL Records
print("The inserted records are")
data = cursor.execute("""Select * From STUDENT""")

# Once we execute this we will store all the information in our data variable.

# Then we will write a for loop 

for row in data:
    print(row)

# What we are saying here is that we want to print every row of data we have.

# This is our entire Query.

# Now we can run this command in our terminal (python sqllite.py), and we should be able to
#generate a table with all of the information we assigned.

# We will also notice that our student.db file is created in our folder.

# This will let us know that our insert was successful.

# Now all of our data has been inserted into our Database.

# This completes our first step of the project.

# In the step we will be creating an LLM application.

# We will be using the DB we created in step one in step two.

# What we want our LLM to do is take some english text as input, and then retrieve
#some records from the DB we created in step 1.

# To get started we will create a new file where we will be writing our code for our LLM.

# The name of this file will be sql.py

# The first thing we will do is import the dot env library.

# This is how we  will do that.

from dotenv import load_dotenv

# To load all of the environment variables we will use this code.

load_dotenv() ## To load all of the environment variables.

# The next thing we will do is import streamlit.

# This is the code we will use to do that.

import streamlit as st

# The next thing we will do is import the operating system library.

import os

# We will also be imorting the sqllite3 package.

# This is how we will do that.

import sqlite3

# The next library we will import is the goolge generative library.

# This is how we will do that.

import google.generativeai as genai

# As uaual, once our imports are done the first thing we want to do is set our API Key.

# This is how we will do that.

# We'll start that process by configuring the API Key.

# This is how we will start that process.

## Configure API Key

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# The next thing we will do is create a function 

# This is how we will start that process.

# First we need to understand that two pieces of information will be going into this function.

# The two pieces of information are the prompt that we are specifically giving, and what the 
#GoogleGemini Model needs to behave like.

## Function To Load Google Gemini Model
def get_gemini_response(question, prompt): # Our function will take two parameters. question is the input
    #we are giving.
    model = genai.GenerativeModel("Gemini-Pro")
    # Now we will create our response. This generate_content function is important because it will take 
    #two parameters. The first will determine what the model will act like. So we will pass in prompt, in 
    #as our first parameter, and question as our seccond parameter, in the form of a list.
    response = model.generate_content([prompt[0],question])
    # Next we want to return our response.
    return response.text

# So this entire function is responsible for giving our query.

# The next function we are going to write is the retriever function.

# This is how we will do that.

# The first parameter inside our function will be sql.

# The second parameter will be our db.

# The next thing we will do is create a connection to sqlite 3 using the connect function
#and pass our db as a parameter.

# The next thing we will do is create our cursor.

# This cursor will be responsible for executing our sql query, by way of specifying it by passing
#it as a parameter to execute method.

# Once we get all thre results by executing the sql query, we will perform a fetchall to retrieve all 
#of the records.

# To be able to retrieve, or print the rows we will use a for loop.

# The next thing we will do is return all of the rows.

## Function To retrieve query from Database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    return rows

# The next step we will be taking is defining our prompt.

# This is how we will do that.

# The prompt will be responsible for making the model run efficiently.

# This prompt will be in the form of a list.

# This will be the main aim of the prompt.

## Define Our Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL Query!
    The SQL Database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION \n\nFor example, \nExample 1 - How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    also the sql query should not have ''' in the beginning or the end of the query   

    """
]

# This is our prompt.

# Note: We can ask our model multiple questions at once.

# That would look something like this.

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

# The next step will be to set up our streamlit.

# This is how we will do that.

# We will start by configuring our page using the config function.

# This config function will take a parameter, which will be the title of our page.

# Then we will add a header.

# The header is what we will title our model.

# The next thing we will do is create a text box that will take our inputs in the form of questions.

# We will use an input function to do this.

# The input function will take as parameter "Input", which is the que to enter the users questions.

# We will also use another parameter, which will be "key".

# This parameter will allow us to enter any key in our input text box.

# The next step will be to create a submit button.

# We will do that with a button function which will have a prompt as a parameter.

# The next thing to do is to define what happens if submit is clicked.

# If submit is clicked we want to generate a response to the question we entered into the text box.

# Remember that our prompt is in the form of a list, so inside the repsonse = model.generate_content section
#our def get_gemini_response, we have to indicate which prompt we want to use (in cases of multiple prompts)
#by indexing into prompt. see line 242 for example.

# The next thing we want to do is at a precursor to our response.

# We can do this by using a subheader function, which will take as a parameter the caption "The Response Is".

# Then we will use a for loop to iterate through all the responses.

# This will allow us to print our response.

# We can do that by using a print function to print every row in the response.

# Then we will use another header to display the rows. 

# The next thing we will do is adjust our code so that we can call our response.

# We will do that by calling our read_sql_query function.

# Inside the read sql query function we will pass two parameters. 

# The parameters will be response and the name of our database which is student.db

# Now we should be able to get our response.

# In case we need to debug or just do a system check, we can print out our response in the if
#submit statement.

## Streamlit App
st.set_page_config(page_title = "Para La Casa De Gates")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key = "input")

submit = st.button("Submit Your Question Here")

## If Submit Is Clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    response = read_sql_query(response, "student.db")
    st.subheader("The Response Is")
    for row in response:
        print(row)
        st.header(row)

# We will also add a commit and close to our code to help with execution errors.

# This is how we will do that.

## Commit Changes To The Database
connection.commit()
connection.close()

# The last thing we will do is create a new field in our student table.

# We will name this new field "SCORES".

# This is how we will do that.

table_info = """
Create Table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), SCORES INT);
"""

cursor.execute("""Insert Into Student values("Brian", "Generative AI", "Models", 100)""")
cursor.execute("""Insert Into Student values("Alia", "Media Marketing", "Influencer", 100)""")
cursor.execute("""Insert Into Student values("Delia", "Work & Travel", "Multitasking", 100)""")
cursor.execute("""Insert Into Student values("Bam Bam", "World Studies", "Leadership", 100)""")
cursor.execute("""Insert Into Student values("Amelia", "Business & Finance", "Corporate Management", 100)""")

# If we want to compare the modified version to the original version we can see lines 108 - 130.

# Once we modidy our table, we will delete the current database to make move for the new one.

# Before we access this new database in streamlit we have to create it with our modified table.

# we can do that be running sqllite.py, or which name ever name we gave to the file where we
#created our table.

# Once that file is run and compiled, our updated database will be created and we can now begin
#to query it. 

# 

# Timestamp 27:24:00 
import sqlite3

## Connect To SQLlite Database
connection = sqlite3.connect("student.db")

## Create Curor Object To Insert Records or Create Table
cursor = connection.cursor()

## Create the Table
#table_info = """
#Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25));
#"""

table_info = """
Create table STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    SCORES INT
);
"""

cursor.execute(table_info)

## Insert More Records
cursor.execute("""Insert Into Student values("Brian", "Generative AI", "Models", 100)""")
cursor.execute("""Insert Into Student values("Alia", "Media Marketing", "Influencer", 100)""")
cursor.execute("""Insert Into Student values("Delia", "Work & Travel", "Multitasking", 100)""")
cursor.execute("""Insert Into Student values("Bam Bam", "World Studies", "Leadership", 100)""")
cursor.execute("""Insert Into Student values("Amelia", "Business & Finance", "Corporate Management", 100)""")

## Display ALL Records
print("The inserted records are")
data = cursor.execute("""SELECT * From STUDENT""")

for row in data:
    print(row)

## Commit Changes To The Database
connection.commit()
connection.close()
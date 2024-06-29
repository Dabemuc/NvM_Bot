import sqlite3
from sqlite3 import Error

create_sounds_table = """
CREATE TABLE IF NOT EXISTS sounds (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  fileName TEXT NOT NULL
);
"""


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print("The Error {} occurred".format(e))

    return connection


def execute_write_query(query):
    cursor = con.cursor()
    try:
        cursor.execute(query)
        con.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(query):
    cursor = con.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


con = create_connection("./SQLiteTestDB")
execute_write_query(create_sounds_table)


""" if input ("Do you want to configure Database? (y/n): ") == "y":
    print("Enter SQL-Commands (2x Enter executes command):")
    SQLCommand = ""
    while True:
        inp = input()
        if inp == "":
            while True:
                q = input("Which type of query shall be executed? (write, read) ")
                if q == "write":
                    execute_write_query(SQLCommand)
                    SQLCommand = ""
                    break
                if q == "read":
                    result = execute_read_query(SQLCommand)
                    for sound in result:
                        print(sound)
                    SQLCommand = ""
                    break
                print("Please enter valid query type!")
        else:
            SQLCommand = SQLCommand + "\n" + inp """

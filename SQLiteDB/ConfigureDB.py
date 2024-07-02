import importlib

db = importlib.import_module("DBMS")

print("Enter SQL-Commands (2x Enter executes command):")
SQLCommand = ""
while True:
    inp = input()
    if inp == "":
        while True:
            q = input("Which type of query shall be executed? (write, read) ")
            if q == "write":
                db.execute_write_query(db.con, SQLCommand)
                SQLCommand = ""
                break
            if q == "read":
                result = db.execute_read_query(db.con, SQLCommand)
                for sound in result:
                    print(sound)
                SQLCommand = ""
                break
            print("Please enter valid query type!")
    else:
        SQLCommand = SQLCommand + "\n" + inp
import importlib

#db = importlib.import_module("DBMS")
import SQLiteDB.DBMS as db


def getFileName(name):
    temp = str(db.execute_read_query(db.con, "SELECT fileName FROM sounds WHERE name = '{}'".format(name)))
    mp3ToPlay = temp.replace("[('", "")
    return mp3ToPlay.replace("',)]", "")

def getAllSounds():
    temp = str(db.execute_read_query(db.con, "SELECT name FROM sounds"))
    mp3ToPlay = temp.replace("[('", "")
    mp3ToPlay = mp3ToPlay.replace("',), ('", ", ")
    return mp3ToPlay.replace("',)]", "")

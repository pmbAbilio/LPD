import sqlite3


class DatabaseHandler:
    def __init__(self):
        self.connection = sqlite3.connect("Connection_attempts.db")

    def createDatabase(self):
        print("Creating Table Attampts")
        sqlQuery = """CREATE TABLE IF NOT EXISTS Attempts (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    IP text unique not null,
                    Time text not null,
                    Location text not null
                )"""
        self.connection.execute(sqlQuery)

    def insertData(self, data):
        print("Hello world")


dbh = DatabaseHandler()
dbh.createDatabase()

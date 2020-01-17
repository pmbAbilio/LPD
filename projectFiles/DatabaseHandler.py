import sqlite3


class DatabaseHandler:
    def __init__(self):
        self.connection = sqlite3.connect("Connection_attempts.db")
        self.createDatabase()

    def createDatabase(self):
        print("Creating Table Attempts")
        sqlQuery = """CREATE TABLE IF NOT EXISTS Attempts (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    IP text not null,
                    Time text not null,
                    Location text not null,
                    Message text 
                )"""
        self.connection.execute(sqlQuery)

    def insertData(self, data):
        print(data)
        sql = """INSERT INTO Attempts(Time,IP,Location,Message)
              VALUES(?,?,?,?)"""
        cur = self.connection.cursor()
        cur.execute(sql, data)
        self.connection.commit()

    def selectAll(self):
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM Attempts")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    def selectCount(self):
        cur = self.connection.cursor()
        cur.execute(
            "SELECT Location, COUNT(*) FROM Attempts GROUP BY Location ORDER BY COUNT(*) ASC"
        )
        rows = cur.fetchall()
        return rows


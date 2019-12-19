import sqlite3


class DatabaseHandles:
    conn = sqlite3.connect("hashPC.db")

    def createDatabase(self):
        sqlQuery = """CREATE TABLE IF NOT EXISTS hash (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    nome not null,
                    path unique not null,
                    os text not null,
                    hash_md5 text not null,
                    hash_sha1 text not null
                )"""
        conn.execute(sqlQuery)


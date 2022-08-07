import sqlite3
from config import data_base_name

class userDataBase:
    def __init__(self):
        self.conn = sqlite3.connect(data_base_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
    
    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def createTable(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS usersInfo (
                userID INTEGER,
                name TEXT,
                points INTEGER
                )""")

    def insertUser(self, userID, name, points = 0):
        self.conn.execute(f"""
            INSERT INTO usersInfo (userID, name, points)
            VALUES ({userID}, "{name}", {points})
            """)

    def updateUser(self, userID, name, points):
        self.cursor.execute(f"""
            SELECT * FROM usersInfo
            WHERE userID = {userID}
            """)
        answer = self.cursor.fetchone()

        if answer != None:
            self.conn.execute(f"""
                UPDATE usersInfo
                SET points = points + {points}
                WHERE userID = {userID}
                """)
        else:
            self.insertUser(userID, name, points)

    def getTop5(self):
        self.cursor.execute(f"""
            SELECT * FROM usersInfo
            ORDER BY points DESC
            LIMIT 5
            """)
        return self.cursor.fetchall()

    def commit(self):
        self.conn.commit()

    def deleteUser(self, userID):
        self.conn.execute(f"""
            DELETE FROM usersInfo
            WHERE userID = {userID}
            """)
    
    def getUserPoints(self, userID):
        self.cursor.execute(f"""
            SELECT points FROM usersInfo
            WHERE userID = {userID}
            """)
        data = self.cursor.fetchone()
        if str(data) == "None":
            return None
        return data[0]

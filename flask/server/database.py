import sqlite3

class Database:
    def __init__(self):
        self.database = "chat.db"

    def add_user(self, username, real_name):
        sql = "INSERT INTO users (username, real_name) VALUES (?, ?)"
        query_params = (username, real_name)
        self.__perform_insert__(sql, query_params)

    def get_all_users(self):
        sql = "SELECT username, real_name FROM users"
        params = []
        return self.__perform_select__(sql, params)

    def user_exists(self, username):
        sql = "SELECT username FROM users WHERE username = ?"
        params = (username,)
        results = self.__perform_select__(sql, params)
        if len(results):
            return True
        return False


    def __perform_insert__(self, sql, params):
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        conn.close()

    def __perform_select__(self, sql, params):
        conn = sqlite3.connect(self.database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(sql, params)
        results = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return results









#database.add_user("davidlove", "David Love")
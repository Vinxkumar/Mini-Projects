import sqlite3

class chat_history:
    def __init__(self):
        conn = sqlite3.connect("chat_history.db")
        self.cursor = conn.cursor()
        self.cursor.execute("""
                            create table if not exists chat_history(
                                i integer primary key autoincrement,
                                sender text,
                                message text
                            )
                            """)
    def ins(self, sender, message):
        self.cursor.execute("insert into chat_history(sender, message) values(?,?)",(sender, message))
    def fetch(self):
        self.cursor.execute("SELECT sender, message FROM chat_history")
        rows = self.cursor.fetchall()
        return rows
        
        
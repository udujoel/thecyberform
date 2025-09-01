"""Module providing a function printing python version."""

import sqlite3
from datetime import datetime

connection = sqlite3.connect('database.db')

# Create tables
with open('schema.sql', encoding='utf-8') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Posts
POST_INSERT_SQL = "INSERT INTO posts (title, content, author) VALUES (?,?,?)"

cur.execute(POST_INSERT_SQL,
            ('Welcome to TheCyberForum', 'Content for the first post', 'admin')
            )

cur.execute(POST_INSERT_SQL,
            ('Second Post', 'Content for the second post', 'admin')
            )

cur.execute(POST_INSERT_SQL,
            ('Third Post', 'Content for the Third post', 'admin')
            )


# Users

now = datetime.now().isoformat()
cur.execute( "INSERT INTO users (username, name, email, password, member_since) VALUES (?,?,?,?,?)",
            ('admin', 'admin', 'admin@gmail.com', 'admin', now)
            )

connection.commit()
connection.close()

import sqlite3
import datetime

c = sqlite3.connect("database.db")
print("Database launched...")

c.execute(
    """
CREATE TABLE posts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  content TEXT,
  category TEXT,
  date_created CURRENT_TIMESTAMP
)
"""
)

c.execute(
    """
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT,
  password TEXT,
  role INTEGER,
  date_created CURRENT_TIMESTAMP
)
"""
)

import sqlite3

conn = sqlite3.connect("broai.db", check_same_thread=False)
cursor = conn.cursor()

# Tasks
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    task TEXT
)
""")

# Health
cursor.execute("""
CREATE TABLE IF NOT EXISTS health (
    user_id INTEGER,
    sleep INTEGER,
    water INTEGER,
    workout INTEGER
)
""")

# Income
cursor.execute("""
CREATE TABLE IF NOT EXISTS income (
    user_id INTEGER,
    goal INTEGER,
    current INTEGER
)
""")

# Mood
cursor.execute("""
CREATE TABLE IF NOT EXISTS mood (
    user_id INTEGER,
    mood TEXT
)
""")

# Memory
cursor.execute("""
CREATE TABLE IF NOT EXISTS memory (
    user_id INTEGER,
    key TEXT,
    value TEXT
)
""")

conn.commit()
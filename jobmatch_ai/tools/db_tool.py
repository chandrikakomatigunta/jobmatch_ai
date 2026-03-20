# tools/db_tool.py
import sqlite3
from datetime import datetime

DB_PATH = "database/candidates.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS candidates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        score INTEGER,
        strengths TEXT,
        gaps TEXT,
        url TEXT,
        decision TEXT,
        date TEXT
    )''')
    conn.commit()
    conn.close()

def db_insert(name, score, strengths, gaps, url, decision):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO candidates (name, score, strengths, gaps, url, decision, date) VALUES (?, ?, ?, ?, ?, ?, ?)", 
              (name, score, strengths, gaps, url, decision, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    return "Record inserted."

def db_select(name):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM candidates WHERE name=?", (name,))
    row = c.fetchone()
    conn.close()
    return row or "No record found."

def db_list():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    rows = c.execute("SELECT name, score, date FROM candidates").fetchall()
    conn.close()
    if not rows:
        return "No candidates in database."
    return rows

def db_delete(name):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM candidates WHERE name=?", (name,))
    conn.commit()
    deleted = c.rowcount
    conn.close()
    return "Deleted." if deleted else "No record found."

def db_top(limit=3):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    rows = c.execute("SELECT name, score FROM candidates ORDER BY score DESC LIMIT ?", (limit,)).fetchall()
    conn.close()
    return rows or "No data."

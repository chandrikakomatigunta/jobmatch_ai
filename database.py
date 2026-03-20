import sqlite3

# create DB connection
def get_connection():
    conn = sqlite3.connect("jobmatch.db")
    return conn


# create table
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        score INTEGER,
        matched_skills TEXT,
        missing_skills TEXT,
        jd TEXT
    )
    """)

    conn.commit()
    conn.close()


# insert data
def save_candidate(score, matched, missing, jd):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO candidates (score, matched_skills, missing_skills, jd)
    VALUES (?, ?, ?, ?)
    """, (score, str(matched), str(missing), jd))

    conn.commit()
    conn.close()


# fetch all data
def get_all_candidates():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM candidates")
    rows = cursor.fetchall()

    conn.close()
    return rows
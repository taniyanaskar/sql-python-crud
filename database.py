import sqlite3

def create_table():
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()

    # Create table if it doesn't exist
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        age INTEGER
    )
    ''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()

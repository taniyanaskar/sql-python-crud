import sqlite3

# Insert a new user into the database
def insert_user(name, email, age):
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
        conn.commit()
        print("User inserted successfully!")
    except sqlite3.IntegrityError:
        print("Error: User with this email already exists.")
    finally:
        conn.close()

# Fetch all users from the database
def fetch_users():
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    conn.close()
    return rows

# Update an existing user's data
def update_user(user_id, name=None, email=None, age=None):
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()

    if name:
        cur.execute("UPDATE users SET name = ? WHERE id = ?", (name, user_id))
    if email:
        cur.execute("UPDATE users SET email = ? WHERE id = ?", (email, user_id))
    if age:
        cur.execute("UPDATE users SET age = ? WHERE id = ?", (age, user_id))

    conn.commit()
    conn.close()

# Delete a user from the database
def delete_user(user_id):
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()

    cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

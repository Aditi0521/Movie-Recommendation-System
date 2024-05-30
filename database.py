import sqlite3

def create_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS history (
        history_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        movie_id INTEGER,
        title TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(user_id)
    )
    ''')

    conn.commit()
    conn.close()

def create_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    try:
        # Check if the username already exists
        c.execute('SELECT * FROM users WHERE username = ?', (username,))
        existing_user = c.fetchone()
        if existing_user:
            raise ValueError("Username already exists. Please choose a different username.")

        # Insert the new user
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        print("User created successfully.")
    except sqlite3.IntegrityError as e:
        # Handle UNIQUE constraint violation
        print(f"Error: {e}")
        raise
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    data = c.fetchone()
    conn.close()
    return data

def save_recommendation(user_id, movie_id, title):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO history (user_id, movie_id, title) VALUES (?, ?, ?)', (user_id, movie_id, title))
    conn.commit()
    conn.close()

def fetch_history(user_id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT title, timestamp FROM history WHERE user_id = ? ORDER BY timestamp DESC', (user_id,))
    data = c.fetchall()
    conn.close()
    return data

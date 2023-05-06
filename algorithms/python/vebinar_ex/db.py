import sqlite3


try:
    conn = sqlite3.connect('test_sqlite3.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        user_id INTEGER UNIQUE NOT NULL,
        join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS records(
        id INTEGER PRIMARY KEY,
        user_id INTEGER UNIQUE NOT NULL,
        operation BOOLEAN NOT NULL,
        value DECIMAL NOT NULL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY user_id REFERENSES users(user_id)
    );
    """)
except Exception as ex:
    print('Smth was wrong', ex)
finally:
    conn.commit()
    conn.close()

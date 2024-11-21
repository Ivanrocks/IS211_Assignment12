import sqlite3

def create_db():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('hw13.db')
    cursor = conn.cursor()

    # Execute schema.sql to create tables
    with open('schema.sql', 'r') as file:
        schema = file.read()
        cursor.executescript(schema)

    # Commit changes and close connection
    conn.commit()
    conn.close()


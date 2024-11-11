import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('hw13.db')
cursor = conn.cursor()

# Execute schema.sql to create tables
with open('schema.sql', 'r') as file:
    schema = file.read()
    cursor.executescript(schema)

# Insert initial data
cursor.execute("INSERT INTO Students (first_name, last_name) VALUES (?, ?)", ("John", "Smith"))
cursor.execute("INSERT INTO Quizzes (subject, num_questions, quiz_date) VALUES (?, ?, ?)", ("Python Basics", 5, "2015-02-05"))
cursor.execute("""
    INSERT INTO Results (student_id, quiz_id, score) 
    VALUES (
        (SELECT student_id FROM Students WHERE first_name = "John" AND last_name = "Smith"),
        (SELECT quiz_id FROM Quizzes WHERE subject = "Python Basics" AND quiz_date = "2015-02-05"),
        85
    )
""")

# Commit changes and close connection
conn.commit()
conn.close()

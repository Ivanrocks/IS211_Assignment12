import sqlite3
def db_connection():
    conn = sqlite3.connect('hw13.db')
    cursor = conn.cursor()
    return cursor,conn

def create_database():

    cursor,conn = db_connection()
    with open('schema.sql', 'r') as file:
        schema = file.read()
        cursor.executescript(schema)
    # Commit changes and close the connection
    conn.commit()
    conn.close()
"""
def query_by_user_name(userName):
    cursor, conn = db_connection()
    user = None
    try:
        user = cursor.execute(
            "SELECT * FROM users WHERE username = ?", (userName,)
        ).fetchall()
        conn.commit()
    except Exception as e:
        print(f"Error deleting task: {e}")
    finally:
        # Close the connection after the operation
        conn.close()
        return user
"""
def fetch_students():
    cursor, conn = db_connection()
    try:
        query = "SELECT student_id, first_name, last_name FROM Students"
        students = cursor.execute(query).fetchall()
        return students
    except Exception as e:
        print(f"Error fetching students: {e}")
        return []
    finally:
        conn.close()

def fetch_quizzes():
    cursor, conn = db_connection()
    try:
        query = "SELECT quiz_id, subject, num_questions, quiz_date FROM Quizzes"
        quizzes = cursor.execute(query).fetchall()
        print(quizzes)
        return quizzes
    except Exception as e:
        print(f"Error fetching quizzes: {e}")
        return []
    finally:
        conn.close()

def add_quiz(subject, num_questions, quiz_date):
    # Assuming you have a function for getting the database connection
    cursor, conn = db_connection()

    try:
        cursor.execute(
            "INSERT INTO Quizzes (subject, num_questions, quiz_date) VALUES (?, ?, ?)",
            (subject, num_questions, quiz_date)
        )
        conn.commit()  # Commit changes to the database
    except Exception as e:
        conn.rollback()  # Rollback in case of an error
        raise e
    finally:
        conn.close()# Always close the connection

def add_student(first_name, last_name):
    # Assuming you have a function for getting the database connection
    cursor, conn = db_connection()

    try:
        cursor.execute(
            "INSERT INTO Students (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        conn.commit()  # Commit changes to the database
    except Exception as e:
        conn.rollback()  # Rollback in case of an error
        raise e
    finally:
        conn.close()  # Always close the connection

def authenticate_user(userName, password):
    cursor, conn = db_connection()
    user = None
    try:
        # Verify the username and password
        user = cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?", (userName, password)
        ).fetchone()
        print(user)
        conn.commit()
        return user is not None
    except Exception as e:
        print(f"Error matching user password: {e}")
        return False
    finally:
        # Close the connection after the operation
        conn.close()

def get_quiz_results(student_id):
    # Connect to the database
    cursor, conn = db_connection()

    # Query to get the student's quiz results from the Results table
    query = '''
            SELECT q.quiz_id, q.subject, r.score, q.quiz_date
            FROM Results r
            JOIN Quizzes q ON r.quiz_id = q.quiz_id
            WHERE r.student_id = ?;
        '''

    results = conn.execute(query, (student_id,)).fetchall()

    # Close the database connection
    conn.close()
    return results

def insert_quiz_result(student_id, quiz_id, score):
    cursor, conn = db_connection()
    cursor.execute(
        "INSERT INTO results (student_id, quiz_id, score) VALUES (?, ?, ?)",
        (student_id, quiz_id, score )
    )

    # Close the database connection
    conn.commit()
    conn.close()
    return True
import os

from werkzeug.security import generate_password_hash
from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import dbutility
# Initialize the Flask web application
app = Flask(__name__)
app.secret_key = os.urandom(24)

# A function to check if the user is authenticated (i.e., logged in)
def is_authenticated():
    return 'user_id' in session

@app.route('/')
def index():
    # Redirect to dashboard if already logged in
    if is_authenticated():
        return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route("/dashboard")
def dashboard():
    if not is_authenticated():
        return redirect(url_for('login'))

    students = dbutility.fetch_students()
    quizzes = dbutility.fetch_quizzes()

    return render_template('dashboard.html', students=students, quizzes=quizzes)

@app.route('/login', methods=('GET', 'POST'))
def login():
    if is_authenticated():
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user = dbutility.authenticate_user(username,password)

        if user is False:

            error = 'Incorrect username.'
            print(error)

        if error is None:
            session.clear()
            session['user_id'] = username
            print("User authenticated")
            return redirect(url_for('dashboard'))

        flash(error)

    return render_template('login.html')

@app.route('/student/add', methods=['GET', 'POST'])
def add_student():
    if not is_authenticated():
        return redirect(url_for('login'))

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        error = None

        # Check if both first name and last name are provided
        if not first_name:
            error = 'First name is required.'
        elif not last_name:
            error = 'Last name is required.'

        if error is None:
            try:
                # Add the student to the database
                dbutility.add_student(first_name, last_name)
                return redirect(url_for('dashboard'))  # Redirect to dashboard after success
            except Exception as e:
                error = f"Error adding student: {e}"

        flash(error)

    return render_template('add_student.html')

@app.route('/quiz/add', methods=['GET', 'POST'])
def add_quiz():
    if not is_authenticated():
        return redirect(url_for('login'))

    if request.method == 'POST':
        subject = request.form['subject']
        num_questions = request.form['num_questions']
        quiz_date = request.form['quiz_date']
        error = None

        # Validate form fields
        if not subject:
            error = 'Subject is required.'
        elif not num_questions.isdigit() or int(num_questions) <= 0:
            error = 'Number of questions must be a positive integer.'
        elif not quiz_date:
            error = 'Quiz date is required.'

        if error is None:
            try:
                # Add the quiz to the database
                dbutility.add_quiz(subject, int(num_questions), quiz_date)
                return redirect(url_for('dashboard'))  # Redirect to dashboard after success
            except Exception as e:
                error = f"Error adding quiz: {e}"

        flash(error)

    return render_template('add_quiz.html')


@app.route('/student/<int:student_id>')
def student_results(student_id):
    if not is_authenticated():
        return redirect(url_for('login'))
    results = dbutility.get_quiz_results(student_id)
    print(results)
    # If there are no results, display a "No Results" message
    if not results:
        print("no results")
        return render_template('student_results.html', student_id=student_id, results=None)

    # Otherwise, render the results in a table
    return render_template('student_results.html', student_id=student_id, results=results)


@app.route('/results/add', methods=['GET', 'POST'])
def add_quiz_result():
    if not is_authenticated():
        return redirect(url_for('login'))

    if request.method == 'POST':
        student_id = request.form['student_id']
        quiz_id = request.form['quiz_id']
        score = request.form['score']

        # Basic validation
        if not student_id or not quiz_id or not score:
            flash('Please fill out all fields', 'error')
            return redirect(url_for('add_quiz_result'))

        try:
            # Add the quiz result to the database
            print("Adding quiz")
            dbutility.insert_quiz_result(student_id, quiz_id, score)

            flash('Quiz result added successfully!', 'success')
            return redirect(url_for('dashboard'))
        except Exception as e:
            print(e)
            flash(f'Error adding quiz score: {str(e)}', 'error')

    # Fetch the students and quizzes to populate the dropdowns
    students = dbutility.fetch_students()
    quizzes = dbutility.fetch_quizzes()

    return render_template('add_quiz_result.html', students=students, quizzes=quizzes)


@app.route('/logout')
def logout():
    # Clear session to log out the user
    session.clear()
    print("User logged out")
    return redirect(url_for('login'))

if __name__ == "__main__":
    print("Creating Database.......")
    dbutility.create_database()
    print("Database Created.")
    print("Starting application")
    app.run()

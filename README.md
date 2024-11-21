# IS211_Assignment12
IS211_Assignment12

# Flask Quiz Management System

This is a Flask-based web application designed for managing students, quizzes, and their results. It features user authentication and a dashboard to add and view data.

## Features

1. **User Authentication**  
   - Users must log in to access the dashboard and other functionalities.

2. **Dashboard**  
   - Displays lists of students and quizzes.

3. **Student Management**  
   - Add new students to the database.

4. **Quiz Management**  
   - Add new quizzes with subject, number of questions, and quiz date.

5. **Quiz Results**  
   - Add results for a specific quiz and view a student's quiz results.

6. **User Logout**  
   - Securely log out by clearing the session.

## Routes

| Route                  | Methods | Description                                             |
|------------------------|---------|---------------------------------------------------------|
| `/`                   | GET     | Login page or redirect to the dashboard if logged in.   |
| `/dashboard`          | GET     | Displays lists of students and quizzes.                |
| `/login`              | GET, POST | User login functionality.                             |
| `/student/add`        | GET, POST | Add a new student.                                     |
| `/quiz/add`           | GET, POST | Add a new quiz.                                        |
| `/student/<int:id>`   | GET     | View quiz results for a specific student.              |
| `/results/add`        | GET, POST | Add results for a quiz.                                |
| `/logout`             | GET     | Logs the user out by clearing the session.             |

## Setup Instructions

### Prerequisites

- Python 3.7+
- Flask
- Werkzeug
- `dbutility` module (custom database utility module)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/flask-quiz-management.git
   cd flask-quiz-management
   
# Contributor
Ivan Martinez

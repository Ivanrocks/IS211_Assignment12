-- Table for storing student information
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Quizzes;
DROP TABLE IF EXISTS Results;



CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

-- Table for storing quiz information
CREATE TABLE Quizzes (
    quiz_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
    num_questions INTEGER NOT NULL,
    quiz_date DATE NOT NULL
);

-- Table for linking students to quizzes with their scores
CREATE TABLE Results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    quiz_id INTEGER,
    score INTEGER CHECK(score >= 0 AND score <= 100),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (quiz_id) REFERENCES Quizzes(quiz_id)
);
-- Not the best password :)
INSERT INTO users (username, password) VALUES ("admin", "admin");
-- Insert a student named "John Smith"
INSERT INTO Students (first_name, last_name) VALUES ("John", "Smith");

-- Insert a quiz with subject "Python Basics", 5 questions, given on February 5, 2015
INSERT INTO Quizzes (subject, num_questions, quiz_date) VALUES ("Python Basics", 5, "2015-02-05");

-- Insert a result linking "John Smith" to the "Python Basics" quiz with a score of 85
INSERT INTO Results (student_id, quiz_id, score) VALUES (
    (SELECT student_id FROM Students WHERE first_name = "John" AND last_name = "Smith"),
    (SELECT quiz_id FROM Quizzes WHERE subject = "Python Basics" AND quiz_date = "2015-02-05"),
    85
);

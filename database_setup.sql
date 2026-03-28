-- Create Students Table
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    email TEXT
);

-- Create Courses Table
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT
);

-- Create Enrollments Table
CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    course_id INTEGER,
    date TEXT,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(course_id) REFERENCES courses(id)
);

-- Insert Sample Data
INSERT INTO students (name, age, email) VALUES ('Alvine', 22, 'alvine@email.com');
INSERT INTO students (name, age, email) VALUES ('Brian', 24, 'brian@email.com');

INSERT INTO courses (course_name) VALUES ('Databases');
INSERT INTO courses (course_name) VALUES ('Web Development');

INSERT INTO enrollments (student_id, course_id, date) VALUES (1, 1, '2025-03-01');
INSERT INTO enrollments (student_id, course_id, date) VALUES (2, 2, '2025-03-05');
import sqlite3

# =========================
# CONNECT DATABASE
# =========================
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

print(" Database connected successfully\n")

# =========================
# CREATE TABLES
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    email TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS enrollments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    course_id INTEGER,
    date TEXT,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(course_id) REFERENCES courses(id)
)
""")

conn.commit()
print("Tables created successfully\n")

# =========================
# FUNCTIONS
# =========================
def add_student(name, age, email):
    cursor.execute("INSERT INTO students (name, age, email) VALUES (?, ?, ?)", (name, age, email))
    conn.commit()

def add_course(course_name):
    cursor.execute("INSERT INTO courses (course_name) VALUES (?)", (course_name,))
    conn.commit()

def enroll_student(student_id, course_id, date):
    cursor.execute("INSERT INTO enrollments (student_id, course_id, date) VALUES (?, ?, ?)",
                   (student_id, course_id, date))
    conn.commit()

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("STUDENTS LIST:")
    for row in rows:
        print(row)
    print()

def view_enrollments():
    cursor.execute("""
    SELECT students.name, courses.course_name, enrollments.date
    FROM enrollments
    JOIN students ON students.id = enrollments.student_id
    JOIN courses ON courses.id = enrollments.course_id
    """)

    rows = cursor.fetchall()

    print("ENROLLMENTS:")
    for row in rows:
        print(row)
    print()

def update_student(student_id, new_email):
    cursor.execute("UPDATE students SET email=? WHERE id=?", (new_email, student_id))
    conn.commit()

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

def count_students():
    cursor.execute("SELECT COUNT(*) FROM students")
    print(" Total students:", cursor.fetchone()[0])

def average_age():
    cursor.execute("SELECT AVG(age) FROM students")
    print(" Average age:", cursor.fetchone()[0])

# =========================
# SAMPLE RUN (FOR DEMO)
# =========================
print("Running sample data...\n")

add_student("Alvine", 22, "alvine@email.com")
add_student("Brian", 24, "brian@email.com")
add_student("Sarah", 21, "sarah@email.com")

add_course("Databases")
add_course("Web Development")

enroll_student(1, 1, "2025-03-01")
enroll_student(2, 2, "2025-03-05")
enroll_student(3, 1, "2025-03-10")

view_students()
view_enrollments()

print("Updating student 1 email...\n")
update_student(1, "updated@email.com")
view_students()

print("Deleting student 2...\n")
delete_student(2)
view_students()

count_students()
average_age()

# =========================
# CLOSE CONNECTION
# =========================
conn.close()

print("\n Program finished successfully")
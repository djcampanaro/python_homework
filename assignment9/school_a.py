import pandas as pd
import sqlite3

# Connect to a new SQLite database
# with  sqlite3.connect("../db/school.db") as conn:  # Create the file here, so that it is not pushed to GitHub!
    # print("Database created and connected successfully.")

    # The "with" statement commits successful transactions and rolls back transactions which cause exceptions within the block.  You must close the connection explicitly with conn.close().

    # cursor = conn.cursor()

    # # Create tables
    # cursor.execute("""
    # CREATE TABLE IF NOT EXISTS Students (
    #     student_id INTEGER PRIMARY KEY,
    #     name TEXT NOT NULL UNIQUE,
    #     age INTEGER,
    #     major TEXT
    # )
    # """)

    # cursor.execute("""
    # CREATE TABLE IF NOT EXISTS Courses (
    #     course_id INTEGER PRIMARY KEY,
    #     course_name TEXT NOT NULL UNIQUE,
    #     instructor_name TEXT
    # )
    # """)

    # cursor.execute("""
    # CREATE TABLE IF NOT EXISTS Enrollments (
    #     enrollment_id INTEGER PRIMARY KEY,
    #     student_id INTEGER,
    #     course_id INTEGER,
    #     FOREIGN KEY (student_id) REFERENCES Students (student_id),
    #     FOREIGN KEY (course_id) REFERENCES Courses (course_id)
    # )
    # """)

    # print("Tables created successfully.")

def add_student(cursor, name, age, major):
    try:
        cursor.execute("INSERT INTO Students (name, age, major) VALUES (?,?,?)", (name, age, major))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_course(cursor, name, instructor):
    try:
        cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES (?,?)", (name, instructor))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def enroll_student(cursor, student, course):
    cursor.execute("SELECT * FROM Students WHERE name = ?", (student,)) # For a tuple with one element, you need to include the comma
    results = cursor.fetchall()
    if len(results) > 0:
        student_id = results[0][0]
    else:
        print(f"There was no student named {student}.")
        return
    cursor.execute("SELECT * FROM Courses WHERE course_name = ?", (course,))
    results = cursor.fetchall()
    if len(results) > 0:
        course_id = results[0][0]
    else:
        print(f"There was no course named {course}.")
        return
    cursor.execute("SELECT * FROM Enrollments WHERE student_id = ? AND course_id = ?", (student_id, course_id))
    results = cursor.fetchall()
    if len(results) > 0:
        print(f"Student {student} is already enrolled in course {course}.")
        return
    cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
    print(student_id, course_id)

with sqlite3.connect("../db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
    cursor = conn.cursor()

    # Insert sample data into tables

    # add_student(cursor, 'Jasmine', 20, 'Computer Science')  
    # add_student(cursor, 'Pratik', 22, 'History')
    # add_student(cursor, 'Carlos', 19, 'Biology')
    # add_course(cursor, 'Math 101', 'Dr. Smith')
    # add_course(cursor, 'English 101', 'Ms. Jones')
    # add_course(cursor, 'Chemistry 101', 'Dr. Lee')

    # conn.commit() 
    # If you don't commit the transaction, it is rolled back at the end of the with statement, and the data is discarded.
    # print("Sample data inserted successfully.")

    # cursor.execute("SELECT * FROM Students WHERE name = 'Jasmine'")
    # result = cursor.fetchall()
    # for row in result:
    #     print(row)

    # And at the bottom of your "with" block

    # enroll_student(cursor, "Jasmine", "Math 101")
    # enroll_student(cursor, "Jasmine", "Chemistry 101")
    # enroll_student(cursor, "Pratik", "Math 101")
    # enroll_student(cursor, "Pratik", "English 101")
    # enroll_student(cursor, "Carlos", "English 101")
    # conn.commit() # more writes, so we have to commit to make them final!

    with sqlite3.connect("../db/lesson.db") as conn:
        sql_statement = """SELECT c.customer_name, o.order_id, p.product_name FROM customers c JOIN orders o ON c.customer_id = o.customer_id 
        JOIN line_items li ON o.order_id = li.order_id JOIN products p ON li.product_id = p.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    print(df)

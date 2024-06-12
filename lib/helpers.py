# lib/helpers.py

from db import connect_db

def add_course():
    conn = connect_db()
    cursor = conn.cursor()
    name = input("Enter name of course >>> ")
    category_name = input("Enter course category >>> ")
    institution_name = input("Enter name of institution offering new course >>> ")
    duration = input("Enter duration of course >>> ")
    cost = input("Enter cost of course >>> ")

    cursor.execute('INSERT OR IGNORE INTO categories (name) VALUES (?)', (category_name,))
    cursor.execute('INSERT OR IGNORE INTO institutions (name) VALUES (?)', (institution_name,))
    conn.commit()

    cursor.execute('SELECT id FROM categories WHERE name = ?', (category_name,))
    category_id = cursor.fetchone()[0]

    cursor.execute('SELECT id FROM institutions WHERE name = ?', (institution_name,))
    institution_id = cursor.fetchone()[0]

    cursor.execute('''
    INSERT INTO courses (name, category_id, institution_id, duration, cost)
    VALUES (?, ?, ?, ?, ?)
    ''', (name, category_id, institution_id, duration, cost))

    conn.commit()
    conn.close()
    print(" ")
    print("Bravo!")
    print("Course added successfully!")

def lookup_course():
    name = input("Enter name of course >>> ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM courses WHERE name = (name)')
    course = cursor.fetchone()
    conn.close()
    if course:
        print(course)
    else:
        print(" ")
        print("Ooops Sorry!")
        print("Course not an EduNexa Course")

def view_all_courses():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM courses')
    courses = cursor.fetchall()
    conn.close()
    if not courses:
        print("No courses available.")
    else:
        for course in courses:
            print(course)

def delete_course():
    name = input("Enter name of course >>> ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM courses WHERE name = (name)')
    conn.commit()
    conn.close()
    print(" ")
    print("Course deleted successfully!")

def update_course():
    old_name = input("Enter current name of course >>> ")
    new_name = input("Enter new name of course >>> ")
    category_name = input("Enter new course category >>> ")
    institution_name = input("Enter new name of institution offering new course >>> ")
    duration = input("Enter new duration of course >>> ")
    cost = input("Enter new cost of course >>> ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('INSERT OR IGNORE INTO categories (name) VALUES (?)', (category_name,))
    cursor.execute('INSERT OR IGNORE INTO institutions (name) VALUES (?)', (institution_name,))
    conn.commit()

    cursor.execute('SELECT id FROM categories WHERE name = ?', (category_name,))
    category_id = cursor.fetchone()[0]

    cursor.execute('SELECT id FROM institutions WHERE name = ?', (institution_name,))
    institution_id = cursor.fetchone()[0]

    cursor.execute('''
    UPDATE courses
    SET name = ?, category_id = ?, institution_id = ?, duration = ?, cost = ?
    WHERE name = ?
    ''', (new_name, category_id, institution_id, duration, cost, old_name))

    conn.commit()
    conn.close()
    print(" ")
    print(" Nice!")
    print("Course updated successfully!")

def sort_courses():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM courses ORDER BY name')
    courses = cursor.fetchall()
    conn.close()
    if not courses:
        print("No courses available.")
    else:
        for course in courses:
            print(course)

def view_institutions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM institutions')
    institutions = cursor.fetchall()
    conn.close()
    if not institutions:
        print("Institution not part of EduNexa")
    else:
        for institution in institutions:
            print(institution)

def view_courses_by_institution():
    institution_name = input("Enter name of institution >>> ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT courses.*
    FROM courses
    JOIN institutions ON courses.institution_id = institutions.id
    WHERE institutions.name = ?
    ''', (institution_name,))
    courses = cursor.fetchall()
    conn.close()
    if not courses:
        print("Course not found for this institution.")
    else:
        for course in courses:
            print(course)

def why_choose_edunexa():
    print("*** Why choose an EduNexa course? ***")
    print("  ")
    print("EduNexa is an online platform that provides you with the best courses in the world.")
    print("  ")
    print("EduNexa is a platform that provides you with the best courses in the world.")
    print("  ")

def help():
    print("You seem to be encountering a problem. Please try running the program again.")

def exit_program():
    sure = input("Are you sure you want to terminate the program[y/n]? ")
    if sure.lower() == "y":
        print("  ")
        print("Exiting EduNexa...")
        print("  ")
        print("Goodbye, we hope you enjoyed our services!")
        exit()
    else:
        print("  ")
        print("Returning to EduNexa...")

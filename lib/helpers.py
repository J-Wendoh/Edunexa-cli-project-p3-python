from db import connect_db
from prettytable import PrettyTable 

def add_course():
    conn = connect_db()
    cursor = conn.cursor()
    name = input("Enter name of course >>> ")
    category_name = input("Enter course category >>> ")
    category_description = input("Enter course category description >>> ")
    institution_name = input("Enter name of institution offering new course >>> ")
    institution_location = input("Enter location of the institution >>> ")
    institution_address = input("Enter address of the institution >>> ")
    duration = input("Enter duration of course >>> ")
    cost = input("Enter cost of course >>> ")

    try:
        cursor.execute('INSERT OR IGNORE INTO categories (name, description) VALUES (?, ?)', (category_name, category_description))
        cursor.execute('INSERT OR IGNORE INTO institutions (name, location, address) VALUES (?, ?, ?)', (institution_name, institution_location, institution_address))
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
        print("Bravo!")
        print("Course added successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def lookup_course():
    name = input("Enter name of course >>> ")
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM courses WHERE name = ?', (name,))
        course = cursor.fetchone()
        if course:
            print(course)
        else:
            print("Ooops Sorry!")
            print("Course not an EduNexa Course")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def view_all_courses():
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT name, duration, cost FROM courses')
        courses = cursor.fetchall()
        if not courses:
            print("No courses available.")
        else:
            table = PrettyTable(['Course Name', 'Duration', 'Cost'])
            for course in courses:
                table.add_row([course[0], course[1], course[2]])
            
            print(table)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def view_courses_by_institution():
    institution_name = input("Enter name of institution >>> ")
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
        SELECT courses.name, courses.duration, courses.cost
        FROM courses
        JOIN institutions ON courses.institution_id = institutions.id
        WHERE institutions.name = ?
        ''', (institution_name,))
        courses = cursor.fetchall()
        if not courses:
            print("No courses found for this institution.")
        else:
            table = PrettyTable(['Course Name', 'Duration', 'Cost'])
            for course in courses:
                table.add_row([course[0], course[1], course[2]])
            
            print(table)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def sort_courses():
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT name, duration, cost FROM courses ORDER BY name')
        courses = cursor.fetchall()
        if not courses:
            print("No courses available.")
        else:
            table = PrettyTable(['Course Name', 'Duration', 'Cost'])
            for course in courses:
                table.add_row([course[0], course[1], course[2]])
            
            print(table)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


def delete_course():
    name = input("Enter name of course >>> ")
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM courses WHERE name = ?', (name,))
        conn.commit()
        print("Course deleted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def update_course():
    old_name = input("Enter current name of course >>> ")
    new_name = input("Enter new name of course >>> ")
    category_name = input("Enter new course category >>> ")
    category_description = input("Enter new course category description >>> ")
    institution_name = input("Enter new name of institution offering new course >>> ")
    institution_location = input("Enter new location of the institution >>> ")
    institution_address = input("Enter new address of the institution >>> ")
    duration = input("Enter new duration of course >>> ")
    cost = input("Enter new cost of course >>> ")

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT OR IGNORE INTO categories (name, description) VALUES (?, ?)', (category_name, category_description))
        cursor.execute('INSERT OR IGNORE INTO institutions (name, location, address) VALUES (?, ?, ?)', (institution_name, institution_location, institution_address))
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
        print("Nice!")
        print("Course updated successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()



def view_institutions():
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT name, location, contact_person, address FROM institutions')
        institutions = cursor.fetchall()
        if not institutions:
            print("No institutions available.")
        else:
            table = PrettyTable(['Institution Name', 'Location', 'Contact Person', 'Address'])
            for institution in institutions:
                table.add_row([institution[0], institution[1], institution[2], institution[3]])
            
            print(table)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


        
def view_contacts_by_institution():
    institution_name = input("Enter name of institution >>> ")
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
        SELECT name, phone, email
        FROM contacts
        JOIN institutions ON contacts.institution_id = institutions.id
        WHERE institutions.name = ?
        ''', (institution_name,))
        contacts = cursor.fetchall()
        if not contacts:
            print("No contacts found for this institution.")
        else:
            table = PrettyTable(['Contact Name', 'Phone', 'Email'])
            for contact in contacts:
                table.add_row([contact[0], contact[1], contact[2]])
            
            print(table)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


def add_contact():
    institution_name = input("Enter name of institution >>> ")
    contact_name = input("Enter contact person's name >>> ")
    contact_phone = input("Enter contact person's phone number >>> ")
    contact_email = input("Enter contact person's email >>> ")

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT id FROM institutions WHERE name = ?', (institution_name,))
        institution_id = cursor.fetchone()
        if institution_id:
            institution_id = institution_id[0]
            cursor.execute('''
            INSERT INTO contacts (institution_id, name, phone, email)
            VALUES (?, ?, ?, ?)
            ''', (institution_id, contact_name, contact_phone, contact_email))
            conn.commit()
            print("Contact added successfully!")
        else:
            print("Institution not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


def view_contacts_by_institution():
    institution_name = input("Enter name of institution >>> ")
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
        SELECT contacts.name, contacts.phone, contacts.email
        FROM contacts
        JOIN institutions ON contacts.institution_id = institutions.id
        WHERE institutions.name = ?
        ''', (institution_name,))
        contacts = cursor.fetchall()
        if not contacts:
            print("No contacts found for this institution.")
        else:
            table = PrettyTable(['Contact Name', 'Phone', 'Email'])
            for contact in contacts:
                table.add_row([contact[0], contact[1], contact[2]])
            
            print(table)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

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

from helpers import (
    add_course,
    lookup_course,
    view_all_courses,
    delete_course,
    update_course,
    sort_courses,
    view_institutions,
    view_courses_by_institution,
    add_contact,
    view_contacts_by_institution,
    why_choose_edunexa,
    help,
    exit_program
)
from db import init_db

def main():
    init_db()
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            add_course()
        elif choice == "2":
            lookup_course()
        elif choice == "3":
            view_all_courses()
        elif choice == "4":
            delete_course()
        elif choice == "5":
            update_course()
        elif choice == "6":
            sort_courses()
        elif choice == "7":
            view_institutions()
        elif choice == "8":
            view_courses_by_institution()
        elif choice == "9":
            add_contact()
        elif choice == "10":
            view_contacts_by_institution()
        elif choice == "11":
            why_choose_edunexa()
        elif choice == "12":
            help()
        elif choice == "13":
            exit_program()
        else:
            print("Invalid choice")

def menu():
    print("WELCOME TO EDUNEXA")
    print("*** Where academics meet your time priority ***")
    print(" ")
    print("1) Add a course to EduNexa")
    print("2) Look up course details from EduNexa")
    print("3) View all courses in EduNexa")
    print("4) Delete a course from EduNexa")
    print("5) Update a course in EduNexa")
    print("6) Sort courses in EduNexa")
    print("7) View Institutions EduNexa")
    print("8) View all courses offered by a particular institution")
    print("9) Add contact person for an institution")
    print("10) View contact persons of an institution")
    print("11) Why choose an EduNexa course?")
    print("12) HELP!")
    print(" ")
    print("13) Quit EduNexa")

if __name__ == "__main__":
    main()



from helpers import (
    add_course,
    lookup_course,
    view_all_courses,
    delete_course,
    update_course,
    sort_courses,
    view_institutions,
    view_courses_by_institution,
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
            why_choose_edunexa()
        elif choice == "10":
            help()
        elif choice == "11":
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
    print("9) Why choose an EduNexa course?")
    print("10) HELP!")
    print(" ")
    print("11) Quit EduNexa")

if __name__ == "__main__":
    main()

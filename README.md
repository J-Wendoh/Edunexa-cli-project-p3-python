# EduNexa CLI Project  

Welcome to the EduNexa CLI project! This project aims to provide a command-line interface (CLI) for managing courses, institutions, and users within the EduNexa platform.

## CLI Script

### `lib/cli.py`

This script is the main entry point for the EduNexa CLI. It allows users to interactively manage courses, institutions, and users through a series of prompts and commands.

#### Functions:

- `main()`: This function is the main loop of the CLI. It displays the menu options and handles user input.
- `menu()`: This function displays the menu options for the user to choose from.
- Other functions such as `add_course()`, `lookup_course()`, `delete_course()`, etc., are imported from `lib/helpers.py` and are responsible for performing specific actions based on user input.

## Helper Functions

### `lib/helpers.py`

This module contains helper functions used by the CLI script to perform various tasks such as adding, deleting, and updating courses, as well as interacting with institutions and users.

#### Functions:

- `add_course()`: Adds a new course to the EduNexa platform.
- `lookup_course()`: Looks up details of a specific course.
- `delete_course()`: Deletes a course from the platform.
- `update_course()`: Updates the details of a course.
- Other functions for viewing courses by institution, sorting courses, viewing institutions, etc., are also defined in this module.

## Models

### `lib/models/`

This directory contains Python files defining the data models used in the EduNexa platform. Each model represents a table in the SQLite database.

- `category.py`: Defines the Category model for course categories.
- `institution.py`: Defines the Institution model for institutions offering courses.
- `course.py`: Defines the Course model for individual courses.
- `user.py`: Defines the User model for platform users.

## Database

### `lib/db.py`

This module contains functions for database initialization and connection. It also defines the schema for the SQLite database used by the application.

#### Functions:

- `connect_db()`: Connects to the SQLite database.
- `init_db()`: Initializes the database by creating tables for categories, institutions, courses, and users.

## How to Run the CLI

To run the EduNexa CLI:

1. Clone the repository: `git clone https://github.com/J-Wendoh/Edunexa-cli-project-p3-python.git`
2. Navigate to the project directory: `cd Edunexa-cli-project-p3-python`
3. Install dependencies: `pipenv install`
4. Activate the virtual environment: `pipenv shell`
5. Run the CLI script: `python lib/cli.py`

## Screenshots

[Add screenshots here if available]

## Resources

- [SQLite Documentation](https://www.sqlite.org/docs.html): Official documentation for SQLite database.
- [Python SQLite3 Documentation](https://docs.python.org/3/library/sqlite3.html): Official documentation for Python's SQLite3 module.
- [Markdown Syntax Guide](https://www.markdownguide.org/basic-syntax/): Guide for writing Markdown syntax used in this README.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Author

Joanne Wendoh

Feel free to explore the codebase and contribute to further improvements of the EduNexa CLI project!

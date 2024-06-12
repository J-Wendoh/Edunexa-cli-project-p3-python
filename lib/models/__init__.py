import sqlite3


from lib.db import init_db, connect_db

init_db()

from .course import Course
from .category import Category
from .institution import Institution
from .user import User



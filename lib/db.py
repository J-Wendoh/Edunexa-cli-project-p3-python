import sqlite3

DATABASE = 'edunexa.db'

def connect_db():
    try:
        return sqlite3.connect(DATABASE)
    except sqlite3.Error as e:
        print(f"Database connection failed: {e}")
        return None

def create_table(cursor, create_table_sql):
    try:
        cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(f"Failed to create table: {e}")

def init_db():
    conn = connect_db()
    if conn is None:
        return

    cursor = conn.cursor()
    
    create_table(cursor, '''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT
    )
    ''')
    
    create_table(cursor, '''
    CREATE TABLE IF NOT EXISTS institutions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        location TEXT,
        address TEXT   
    )
    ''')
    
    create_table(cursor, '''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category_id INTEGER NOT NULL,
        institution_id INTEGER NOT NULL,
        duration TEXT NOT NULL,
        cost TEXT NOT NULL,
        FOREIGN KEY (category_id) REFERENCES categories(id),
        FOREIGN KEY (institution_id) REFERENCES institutions(id)
    )
    ''')
    
    create_table(cursor, '''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        institution_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL,
        FOREIGN KEY (institution_id) REFERENCES institutions(id)
    )
    ''')
    
    conn.commit()
    conn.close()

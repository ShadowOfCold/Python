import sqlite3

def create_table():
    with sqlite3.connect("MangaLib.db") as db:
        cursor = db.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS comics(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        title TEXT,
        chapter TEXT,
        link TEXT
        );""")
        db.commit()

def insert_comics(col1, col2, col3, col4):
    with sqlite3.connect("MangaLib.db") as db:
        cursor = db.cursor()
        data_list = (col1, col2, col3, col4)
        cursor.execute("""
                        INSERT INTO comics (type, title, chapter, link)
                        VALUES (?, ?, ?, ?);
                            """, data_list)
        db.commit()

def check_comics(title):
    with sqlite3.connect("MangaLib.db") as db:
        cursor = db.cursor()
        cursor.execute("""SELECT title FROM comics WHERE title = ? """, (title,))
        result = cursor.fetchall()
        if len(result) == 0:
            return False
        else:
            return True
        
def update_comics(chapter):
    with sqlite3.connect("MangaLib.db") as db:
        cursor = db.cursor()
        cursor.execute("""SELECT chapter FROM comics WHERE chapter = ? """, (chapter,))
        result = cursor.fetchall()
        if len(set(result)) == 2:
            cursor.execute("""UPDATE comics SET chapter = ?""", chapter)
        
def get_data_from_db():
    with sqlite3.connect("MangaLib.db") as db:
        cursor = db.cursor()
        cursor.execute("""SELECT type, title, chapter, link FROM comics""")
        data_set = cursor.fetchall()
        return data_set

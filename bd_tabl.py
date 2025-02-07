import sqlite3



# Создаём базу данных
def create_tables():
    con = sqlite3.connect("spisok.db")
    cur = con.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS classes(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS listtodo(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, data TEXT, description TEXT)")

    con.commit()
    con.close()


def list_stranichka(name: str, data: str, description: str):
    con = sqlite3.connect("spisok.db")
    cur = con.cursor()

    cur.execute(
        "INSERT INTO listtodo(name, data, description) VALUES (?, ?, ?)",
        (name, data, description))

    con.commit()
    last_row_id = cur.lastrowid
    con.close()

    return last_row_id


def get_all_todos():
    con = sqlite3.connect("spisok.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM listtodo")
    todos = cur.fetchall()
    con.close()

    return todos


# Удаление из базы данных
def delete_todo(todo_id):
    con = sqlite3.connect("spisok.db")
    cur = con.cursor()

    cur.execute("DELETE FROM listtodo WHERE id = ?", (todo_id,))

    con.commit()
    con.close()

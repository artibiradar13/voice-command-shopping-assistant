import sqlite3
from utils.categories_helper import get_category

DB_NAME = "shopping.db"


# -------------------------
# INIT DATABASE
# -------------------------

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shopping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT UNIQUE,
            quantity INTEGER,
            category TEXT
        )
    """)

    conn.commit()
    conn.close()


# -------------------------
# ADD ITEM
# -------------------------

def add_item(item, qty):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    category = get_category(item)

    cursor.execute("SELECT quantity FROM shopping WHERE item = ?", (item,))
    existing = cursor.fetchone()

    if existing:
        cursor.execute(
            "UPDATE shopping SET quantity = quantity + ? WHERE item = ?",
            (qty, item)
        )
    else:
        cursor.execute(
            "INSERT INTO shopping (item, quantity, category) VALUES (?, ?, ?)",
            (item, qty, category)
        )

    conn.commit()
    conn.close()


# -------------------------
# REMOVE ITEM COMPLETELY
# -------------------------

def remove_item(item):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM shopping WHERE item = ?", (item,))

    conn.commit()
    conn.close()


# -------------------------
# UPDATE QUANTITY (+ / -)
# -------------------------

def update_quantity(item, new_qty):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    if new_qty <= 0:
        cursor.execute("DELETE FROM shopping WHERE item = ?", (item,))
    else:
        cursor.execute(
            "UPDATE shopping SET quantity = ? WHERE item = ?",
            (new_qty, item)
        )

    conn.commit()
    conn.close()


# -------------------------
# GET ITEMS
# -------------------------

def get_items():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT item, quantity, category FROM shopping")
    items = cursor.fetchall()

    conn.close()
    return items


# -------------------------
# CLEAR ALL ITEMS
# -------------------------

def clear_items():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM shopping")

    conn.commit()
    conn.close()


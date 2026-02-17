import sqlite3
from utils.categories_helper import get_category

DB_NAME = "shopping.db"


# -------------------------
# CONNECT
# -------------------------

def connect():

    return sqlite3.connect(DB_NAME)


# -------------------------
# INIT DB
# -------------------------

def init_db():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS shopping_list(

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

from utils.categories_helper import get_category

def add_item(item, quantity):

    conn = sqlite3.connect("shopping.db")
    cursor = conn.cursor()

    category = get_category(item)

    cursor.execute(
        "SELECT quantity FROM shopping_list WHERE item=?",
        (item,)
    )

    result = cursor.fetchone()

    if result:

        new_qty = result[0] + quantity

        cursor.execute(
            "UPDATE shopping_list SET quantity=?, category=? WHERE item=?",
            (new_qty, category, item)
        )

    else:

        cursor.execute(
            "INSERT INTO shopping_list (item, quantity, category) VALUES (?, ?, ?)",
            (item, quantity, category)
        )

    conn.commit()
    conn.close()

# -------------------------
# GET ITEMS
# -------------------------
def get_items():

    conn = sqlite3.connect("shopping.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT item, quantity, category FROM shopping_list"
    )

    items = cursor.fetchall()

    conn.close()

    return items

# -------------------------
# REMOVE ITEM
# -------------------------

def remove_item(item):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(

        "DELETE FROM shopping_list WHERE item=?",

        (item,)
    )

    conn.commit()

    conn.close()



# -------------------------
# UPDATE QTY
# -------------------------

def update_quantity(item, qty):

    conn = connect()

    cursor = conn.cursor()

    if qty <= 0:

        cursor.execute(

            "DELETE FROM shopping_list WHERE item=?",

            (item,)
        )

    else:

        cursor.execute(

            "UPDATE shopping_list SET quantity=? WHERE item=?",

            (qty, item)
        )

    conn.commit()

    conn.close()



# -------------------------
# CLEAR
# -------------------------

def clear_items():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(

        "DELETE FROM shopping_list"
    )

    conn.commit()

    conn.close()
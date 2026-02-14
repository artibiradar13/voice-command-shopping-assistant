import sqlite3

# connect to database
conn = sqlite3.connect("database.db", check_same_thread=False)

cursor = conn.cursor()


# create table
def create_table():

    cursor.execute("""
    
    CREATE TABLE IF NOT EXISTS shopping_list (
    
        item TEXT,
        quantity INTEGER
    
    )
    
    """)

    conn.commit()



# add item
def add_item(item, quantity):

    cursor.execute(

        "INSERT INTO shopping_list (item, quantity) VALUES (?, ?)",

        (item, quantity)

    )

    conn.commit()



# remove item
def remove_item(item):

    cursor.execute(

        "DELETE FROM shopping_list WHERE item = ?",

        (item,)

    )

    conn.commit()



# get all items
def get_items():

    cursor.execute(

        "SELECT * FROM shopping_list"

    )

    return cursor.fetchall()



# search item
def search_item(item):

    cursor.execute(

        "SELECT * FROM shopping_list WHERE item = ?",

        (item,)

    )

    return cursor.fetchall()
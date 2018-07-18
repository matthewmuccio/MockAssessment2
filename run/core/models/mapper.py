#!/usr/bin/env python3


import sqlite3


# Retrieves the item data from the SQLite database file, as a list.
# Example output: [1, "bicycle", 25.0, "photo-1531857475897-48f2102b7566"]
def get_item_data(item_name):
    connection = sqlite3.connect("products.db", check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE name=?", (item_name,))
    try:
        item_data = list(cursor.fetchall()[0])
    except IndexError:
        item_data = []
    cursor.close()
    connection.close()
    return item_data
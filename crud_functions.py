import sqlite3


connection = sqlite3.connect('products.db')
cursor = connection.cursor()

def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')


def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    products_list = cursor.execute("SELECT * FROM Products").fetchall()
    connection.commit()
    return products_list


connection.commit()
connection.close()
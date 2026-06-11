import sqlite3

def create_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (publisher_name) VALUES (?)", (name))
    except sqlite3.IntegrityError:
        print(f"{name[0]} is already in the database.")

def create_magazine(cursor, name, publisher):
    cursor.execute("SELECT publisher_id FROM publishers WHERE publisher_name=?", (publisher,))
    results = cursor.fetchall()
    if len(results) > 0:
        publisher_id = results[0][0]
    try:
        cursor.execute("INSERT INTO magazines (magazine_name, publisher_id) VALUES (?, ?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def create_subscriber(cursor, name, address):
    cursor.execute("SELECT subscribers.address FROM subscribers WHERE name=?", (name,))
    results = cursor.fetchall()
    if address in results[0]:
        print("Subscriber is already in the database.")
        return
    else:
        try:
            cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
        except sqlite3.IntegrityError:
            print(f"{name} is already in the database.")

def subscribe_to_magazine(cursor, subscriber, magazine, expiration_date):
    cursor.execute("SELECT * FROM subscribers WHERE name=?", (subscriber,))
    results = cursor.fetchall()
    if len(results) > 0:
        subscriber_id = results[0][0]
    else:
        print(f"There is no subscriber named {subscriber}.")
        return
    cursor.execute("SELECT * FROM magazines WHERE magazine_name=?", (magazine,))
    results = cursor.fetchall()
    if len(results) > 0:
        magazine_id = results[0][0]
    else:
        print(f"There is no magazine named {magazine}.")
        return
    cursor.execute("SELECT * FROM subscriptions WHERE subscriber_id=? and magazine_id=?", (subscriber_id, magazine_id))
    results = cursor.fetchall()
    if len(results) > 0:
        print("Customer has already been subscribed to this magazine.")
        return
    cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber_id, magazine_id, expiration_date))


# Task 1: Create a New SQLite Database
with sqlite3.connect("../db/magazines.db") as conn:

# Task 2: Define Database Structure
    cursor = conn.cursor()
    conn.execute("PRAGMA foreign_keys = 1")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
                   publisher_id INTEGER PRIMARY KEY,
                   publisher_name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
                   magazine_id INTEGER PRIMARY KEY,
                   magazine_name TEXT NOT NULL UNIQUE,
                   publisher_id INTEGER,
                   FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
                   subscriber_id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   address TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
                   subscription_id INTEGER PRIMARY KEY,
                   subscriber_id INTEGER,
                   magazine_id INTEGER,
                   expiration_date TEXT NOT NULL,
                   FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
                   FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
    )
    """)
# print("tables created succesfully")

# Task 3: Populate Tables with Data
    create_publisher(cursor, ("Con de Nast",))
    create_publisher(cursor, ("Moorish Communications",))
    create_publisher(cursor, ("Old York",))
    create_magazine(cursor, "Vanity Fare", "Con de Nast")
    create_magazine(cursor, "Harrel Borse News", "Moorish Communications")
    create_magazine(cursor, "Old York Magazine", "Old York")
    create_subscriber(cursor, "Leslie Smith", "123 Real Street")
    create_subscriber(cursor, "Joe Johnson", "39 Somewhere Ave")
    create_subscriber(cursor, "Hudson Alter", "7834 Broadway")
    create_subscriber(cursor, "Anna McEntyre", "3 Orange Lane")
    create_subscriber(cursor, "Gertrude Smith", "123 Real Street")
    subscribe_to_magazine(cursor, "Joe Johnson", "Old York Magazine", "6-30-27")
    subscribe_to_magazine(cursor, "Gertrude Smith", "Vanity Fare", "6-30-27")
    subscribe_to_magazine(cursor, "Hudson Alter", "Harrel Borse News", "6-30-27")
    subscribe_to_magazine(cursor, "Leslie Smith", "Vanity Fare", "6-30-27")
    subscribe_to_magazine(cursor, "Anna McEntyre", "Old York Magazine", "6-30-27")
    subscribe_to_magazine(cursor, "Hudson Alter", "Harrel Borse News", "6-30-27")
    conn.commit()

# Task 4: Write SQL Queries
    cursor.execute("SELECT * FROM subscribers;")
    subscribers = cursor.fetchall()
    for row in subscribers:
        print(row)

    cursor.execute("SELECT * FROM magazines ORDER BY magazine_name;")
    magazines = cursor.fetchall()
    for row in magazines:
        print(row)

    cursor.execute("SELECT p.publisher_name, m.magazine_name FROM publishers p JOIN magazines m ON p.publisher_id = m.publisher_id WHERE p.publisher_name = 'Old York';")
    publisher_mags = cursor.fetchall()
    for row in publisher_mags:
        print(row)

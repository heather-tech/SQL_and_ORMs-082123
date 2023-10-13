import sqlite3

db_connection = sqlite3.connect('data.db')
db_cursor = db_connection.cursor()
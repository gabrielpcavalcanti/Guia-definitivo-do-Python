import sqlite3

conn = sqlite3.connect('databaseteste.db')

cursor = conn.cursor()

cursor.execute("DROP TABLE exemplo2")

conn.commit()

conn.close()
import sqlite3

connection = sqlite3.connect('database.db')


with open('db/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO datos (nombre, observaciones) VALUES (?, ?)",
            ('Prueba Fernandez', 'Prueba Observaciones')
            )

connection.commit()
connection.close()

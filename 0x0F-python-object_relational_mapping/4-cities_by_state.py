#!/usr/bin/python3
"""Connects a python script to a database using MySQLdb connector"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3])

    my_cursor = my_db.cursor()
    my_cursor.execute(
            """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states
            ON states.id = cities.state_id
            ORDER BY cities.id
            """
            )

    my_data = my_cursor.fetchall()
    for row in my_data:
        print(row)
    my_cursor.close()
    my_db.close()

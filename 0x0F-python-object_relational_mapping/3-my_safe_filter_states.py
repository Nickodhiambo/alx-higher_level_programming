#!/usr/bin/python3
"""This script connects a Python script to a database using MySQLdb"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3])

    my_cursor = my_db.cursor()

    my_cursor.execute(
            """
            SELECT * FROM states WHERE name=%s ORDER BY states.id
            """, (argv[4], )
            )

    my_data = my_cursor.fetchall()

    for row in my_data:
        print(row)

    my_cursor.close()
    my_db.close()

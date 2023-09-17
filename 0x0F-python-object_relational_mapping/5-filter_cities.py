#!/usr/bin/python3
"""This script connects to a database using MySQLdb connector"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)

    my_cursor = my_db.cursor()
    my_cursor.execute(
            """
            SELECT *
            FROM cities
            INNER JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id ASC;
            """
            )
    my_data = my_cursor.fetchall()
    print(", ".join(cities[2] for cities in my_data if cities[4] == argv[4]))
    my_cursor.close()
    my_db.close()

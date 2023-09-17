#!/usr/bin/python3
"""This script queries a database"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # Connect to database
    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3])

    # Create cursor to interact with database
    my_cursor = my_db.cursor()

    # Query database
    my_cursor.execute(
            """
            SELECT * FROM states WHERE name LIKE BINARY '{}'
            ORDER BY states.id ASC;
            """.format(argv[4])
            )

    # Fetch data returned by query
    my_data = my_cursor.fetchall()

    # Work with data
    for row in my_data:
        print(row)

    # Close cursor
    my_cursor.close()

    # Close database
    my_db.close()

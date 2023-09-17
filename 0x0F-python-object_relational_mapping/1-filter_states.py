#!/usr/bin/python3

"""Connects a python script to a database using MySQLdb"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # Connect to db using command line arguments
    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)

    # Create a cursor object to interact with database
    my_cursor = my_db.cursor()

    # Select data from db
    my_cursor.execute("""SELECT * FROM states WHERE name LIKE
        BINARY 'N%'ORDER BY states.id ASC
        """)

    # Fetch all data returned by SELECT
    my_data = my_cursor.fetchall()

    # Loop through fetched, print results
    for row in my_data:
        print(row)

    # Close all cursors
    my_cursor.close()

    # Close all databases
    my_db.close()

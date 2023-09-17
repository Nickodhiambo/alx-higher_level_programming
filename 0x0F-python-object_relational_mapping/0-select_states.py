#!/usr/bin/python3

"""This script connects a python script to a databse"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    # Connect to 'hbtn_0e_0_usa' db using command-line arguments
    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)

    # Create cursor object to interact with database
    my_cursor = my_db.cursor()

    # Select data from db
    my_cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")

    # Fetch all data returned by SELECT query
    my_data = my_cursor.fetchall()

    # Loop through fetched data, printing each row
    for row in my_data:
        print(row)

    # Close cursor
    my_cursor.close()

    # Close db
    my_db.close()

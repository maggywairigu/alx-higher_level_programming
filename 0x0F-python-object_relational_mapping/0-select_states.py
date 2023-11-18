#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa:
Your script should take 3 arguments:
mysql username, mysql password and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""
import MySQLdb
import sys

username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]


def list_states(username, password, database):
    """
    Connect to the MySQL server
    Create a cursor object to interact with the database
    Execute the SQL query to retrieve states
    Fetch all the rows and display the results
    Close the cursor and database connection
    """
    db = MySQLdb.connect
    (host='localhost', user=username, passwd=password, db=database, port=3306)
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    db.close()


list_states(username, password, database)

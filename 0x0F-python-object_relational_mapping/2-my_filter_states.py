#!/usr/bin/python3
"""
Takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Checks if the correct number of arguments are provided"""
    if len(sys.argv) != 5:
        print("Usage: python list_states.py <username> <password> <database>")
        sys.exit(1)

    """Get command-line arguments"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]

    """Connect to mysql server"""
    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)
        """create a cursor object"""
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (search,))
        states = cursor.fetchall()
        for state in states:
            print(state)

        """Close the cursor and database connection"""
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

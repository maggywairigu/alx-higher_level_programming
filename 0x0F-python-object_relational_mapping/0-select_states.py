#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa:
Your script should take 3 arguments: mysql username,
mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Checks if the correct number of arguments are provided"""
    if len(sys.argv) != 4:
        print("Usage: python list_states.py <username> <password> <database>")
        sys.exit(1)

    """Get command-line arguments"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """Connect to mysql server"""
    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)
        """create a cursor object"""
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()
        for state in states:
            print(state)

        """Close the cursor and database connection"""
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

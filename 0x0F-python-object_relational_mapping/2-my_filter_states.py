#!/usr/bin/python3
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

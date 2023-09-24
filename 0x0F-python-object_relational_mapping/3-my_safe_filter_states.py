#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
Your script should take 4 arguments:
mysql username, mysql password, database name and state name
searched (safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a
MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: python list_states.py <usrname> <passwd> <db> <state>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]

    try:
        db = MySQLdb .connect(host="localhost",
                              port=3306,
                              user=username,
                              passwd=password,
                              db=database)
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
        cursor.execute(query, (search,))
        states = cursor.fetchall()
        for state in states:
            print(state)

        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MYSQL Error:", e)

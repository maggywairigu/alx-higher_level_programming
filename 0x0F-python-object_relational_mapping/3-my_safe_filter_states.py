#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
Usage: 3-my_safe_filter_states.py
<mysql username> <mysql password> <database name> <state name searched>
"""
import MySQLdb
import sys

state = sys.argv[4]
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(query, (state,))
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    db.close()

#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
Your script should take 3 arguments:
mysql username, mysql password and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on
localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python list_names.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM cities ORDER BY id ASC")
        cities = cursor.fetchall()
        for city in cities:
            print(city)

        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

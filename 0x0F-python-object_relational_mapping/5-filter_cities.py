#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
Usage: ./5-filter_cities.py
<username> <password> <database> <state>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `cities` as `c` \
    INNER JOIN `states` as `s` \
    ON `c`.`state_id` = `s`.`id` \
    ORDER BY `c`.`id`")
    print(", ".join([ct[2] for ct in cur.fetchall() if ct[4] == sys.argv[4]]))

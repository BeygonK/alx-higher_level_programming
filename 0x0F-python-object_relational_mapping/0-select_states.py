#!/usr/bin/python3

"""Show states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()

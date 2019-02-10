# !/usr/bin/env python3
# Code relies on five created views, please see README.md for details
import psycopg2, sys
DBNAME = "news"

def connect(database_name):
    # Connect to the PostgreSQL database named 'news'. Returns a database connection
    try:
        db = psycopg2.connect(dbname=database_name)
        cursor = db.cursor()
        return db, cursor
        """
                db, cursor : is a tuple. 
                The first element (db) is a connection to the database.
                The second element (cursor) is a cursor for the database.
        """
    except psycopg2.Error as err:
        print("Unable to connect to the database")
        print(err)
        sys.exit(1)

def answer1(cursor):
    # Answer question 1
    cursor.execute("SELECT count(path) as num, articles.title FROM log\
            JOIN articles on CONCAT('/article/',articles.slug)=log.path\
            GROUP by articles.title ORDER by num desc LIMIT 3;")
    print("What are the most popular three articles of all time?")
    rows = cursor.fetchall()
    for row in rows:
        print('"{}"'.format(row[1]), '- {} views'.format(row[0]))

def answer2(cursor):
    # Answer question 2
    cursor.execute("SELECT name, SUM(view2.num) FROM view1, view2\
            where view1.title = view2.title\
            GROUP by name ORDER by sum desc;")
    print("Who are the most popular article authors of all time?")
    rows = cursor.fetchall()
    for row in rows:
        print('"{}"'.format(row[0]), '- {} views'.format(row[1]))

def answer3(cursor):
    # Answer question 3
    cursor.execute("SELECT * FROM view5 where error_percent > 1.0;")
    print("On which days did more than 1% of requests lead to errors?")
    rows = cursor.fetchall()
    for row in rows:
        print('"{}"'.format(row[0]), '- {}% errors'.format(row[1]))

def run():
    # Running report
    print("Running reporting tools...\n")
    db, cursor = connect(DBNAME)
    answer1(cursor)
    print("\n")

    answer2(cursor)
    print("\n")

    answer3(cursor)
    print("\n")

if __name__ == '__main__':
    run()
else:
    print('Importing ...')


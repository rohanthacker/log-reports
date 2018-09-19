#!/usr/bin/env python3
import sys
import psycopg2
import output
import messages as msg
from time import time
from settings import FILENAME, REPORT, DB_CONN

db = None
cursor = None


def make_db_connection():
    global cursor, db
    try:
        db = psycopg2.connect(DB_CONN)
        cursor = db.cursor()
        print(msg.DB_CONN_SUCCESS, '\n')
    except:
        print(msg.DB_CONN_FAILED, '\n')


def write_file(data):
    try:
        f = open(FILENAME, 'r')
        f.write(data)
        f.close()
    except:
        print('Unable to write file, output is displayed below \n')
        print(data)
        sys.exit()


def make_report():
    global cursor
    global db
    data = output.make_header()
    for q in REPORT:
        print(msg.LOG_QUERY_PREFIX, q['title'])
        sql_timer_start = time()
        cursor.execute(q['sql'])
        sql_timer_end = time()
        print('   ', '* finished in {}s'.format(
            round(sql_timer_end - sql_timer_start, 2)), '\n'
            )
        data += output.make_title(q['title'])
        for row in cursor:
            data += q['format'](row)
        data += '\n'
    db.close()
    return data


def main():
    print(output.make_title(msg.MAIN_START))
    make_db_connection()
    data = make_report()
    try:
        write_file(data)
        print(msg.LOG_END)
        print(output.get_full_filename(FILENAME))
    except:
        print('Unable to write file, printing report below \n')
        print(data)
    sys.exit()


if __name__ == '__main__':
    main()

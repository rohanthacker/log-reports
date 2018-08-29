import sys
from datetime import date
from datetime import time
import psycopg2

# Settings
filename = 'helloworld.txt'
q1 = "SELECT * FROM articles LIMIT 3"
q2 = "SELECT * FROM authors"
q3 = "SELECT * from (SELECT date_trunc, SUM(count) from (SELECT date_trunc('day', time), status, COUNT(status) FROM log GROUP BY date_trunc('day',time), status ORDER BY date_trunc('day', time), status) as hits GROUP BY hits.date_trunc) as total GROUP BY total.date_trunc, total.sum"

queries = [
    {'title': 'Top Articles', 'sql': q1,'format': (lambda row: '{} {} \n'.format(row[0], row[1]))},
    {'title': 'Top Authors', 'sql': q2,'format': (lambda row: '{} {} \n'.format(row[0], row[1]))},
    {'title': 'Errors', 'sql': q3, 'format': (lambda row: '{} \n'.format(row))}
    # {'title': 'Errors', 'sql': q3, 'format': (lambda row: '{} \n'.format(row[0].strftime("%D"), row[1]))}
]



def write_file(data):
    f = open(filename,'w')
    f.write(data)
    f.close()
    print("Saved to File ", filename)

def run():
    print("Running...")
    # Connect to DB
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()

    data = ''
    for q in queries:
        cursor.execute(q['sql'])
        data += q['title'] + '\n'
        data += '\n'
        for row in cursor:
            data += q['format'](row)
        data += '\n'            
    write_file(data)
    db.close()

    sys.exit()


if __name__ == '__main__':
    run()
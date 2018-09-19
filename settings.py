'''
    This file controls the output of log-reporter, the main settings in this file are:
    * Filename - Output filename 
    * Report - Handles Output entries in the output
'''

import queries as sql



# The database connection string. Usually consists of dbname and credentials 
DB_CONN = "dbname=news"

# The filename to be used including .format
FILENAME = 'output.txt'


'''
    Report entries must an array of dicts, each having the keys:
        title : STRING Title to be printed above sql output
        sql: STRING SQL query for desired output
        format: FUNC Format function for each row in output, 
                the func will receive row as its only arg
'''
REPORT = [
    {
        'title': 'Top Articles',
        'sql': sql.query_1,
        'format': (lambda row: '{} \n'.format(row[0]))
    },
    {
        'title': 'Top Authors',
        'sql': sql.query_2,
        'format': (lambda row: '{} - ({} Views) \n'.format(row[0], row[1]))
    },
    {
        'title': 'Days with Errors > 1%',
        'sql': sql.query_3,
        'format': (lambda row: '{} \n'.format(row[0].date()))
    }
]

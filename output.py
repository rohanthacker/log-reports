import os
from datetime import date


def make_header():
    title = '*' * 4 + ' LOG REPORT ' + '*' * 4 + '\n'
    title += 'Report Date : ' + str(date.today()) + '\n'
    title += '\n'
    return title


def make_title(title):
    return '{}\n{}\n'.format(title,  '*' * len(title))


def get_full_filename(filename):
    return '{}/{}'.format(os.getcwd(), filename)

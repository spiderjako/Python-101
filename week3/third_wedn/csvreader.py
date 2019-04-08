import csv
import sys

def filter_by_one(file, full_nam):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(' '.join(row))
            else:
                print(' '.join(row))
            line_count += 1


file = sys.argv

filter_by_one(file[1], 'Diana Harris')
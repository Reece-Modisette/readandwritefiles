#   program that reads the file customers.csv and produces a new file containing
# the customer name and country they are from.

import csv
import os

# Global Constants
CUSTFILE = 'customers.csv'

# MAIN--------------------------------------------------------------------------------------


def main():
    # open file for READING:
    infile = open(CUSTFILE, 'r', newline='')

    # create reader object
    reader = csv.reader(infile)

    # skip field names row
    next(reader)

    # Loop through reader
    i = 0
    for row in reader:
        # assign variable name
        l_name = row[1]
        f_name = row[2]
        cntry = row[4]
        i += 1
        print('    ', format(l_name, '10'),
              format(f_name, '15'), format(cntry, '8'))
    print()


main()

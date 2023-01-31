# customer_sales_report.py - program that reads the sales.csv file and creates a new file with the
#   customer ID and calculated total.

import csv
import os

# Global Constants
SALES = 'sales.csv'

# MAIN--------------------------------------------------------------------------------------


def main():
    # open file for READING:
    infile = open(EMPFILE, 'w', newline='')

    # create reader object
    writer = csv.writer(infile)

    # skip field names row
    next(writer)

    # Loop through reader
    i = 0
    for row in reader:
        # assign variable name
        empid = row[0]
        f_name = row[1]
        l_name = row[2]
        sal = row[3]
        bon = row[4]
        i += 1
        print('    ', format(empid, '4'), format(f_name, '10'), format(l_name, '16'),
              format(sal, '7'), format(bon, '6'))
    print()


main()

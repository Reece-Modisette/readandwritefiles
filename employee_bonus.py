#   employee_bonus.py - program that reads the EmployeePay.csv file and prints
# out details of each employee
import csv
import os

# Global Constants
EMPFILE = 'EmployeePay.csv'

# MAIN--------------------------------------------------------------------------------------


def main():
    # open file for READING:
    infile = open(EMPFILE, 'r', newline='')

    # create reader object
    reader = csv.reader(infile)

    # skip field names row
    next(reader)

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

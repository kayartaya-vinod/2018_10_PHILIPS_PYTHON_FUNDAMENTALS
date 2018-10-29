'''
This module has functions related to Date.
is_leap --> returns True or False for the input year
max_days_in_year --> returns maximum days of the input year
max_days_in_month --> returns maximum days of the input month/year
date_serial --> returns the difference between input d/m/y and 1/1/1900
'''

def is_leap(year):
    return year%400==0 or (year%4==0 and year%100!=0)

def max_days_in_year(year):
    return 366 if is_leap(year) else 365

def max_days_in_month(month, year):
    if month==2:
        return 29 if is_leap(year) else 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31
    
def date_serial(date, month, year):
    ds = 0
    for y in range(1900, year):
        ds += max_days_in_year(y)

    for m in range(1, month):
        ds += max_days_in_month(m, year)

    ds += date
    return ds

def main():
    d = int(input('Enter day of the nonth: '))
    m = int(input('Enter the month: '))
    y = int(input('Enter the year: '))
    ds = date_serial(d, m, y)
    print('Date serial for the input date is: ' + str(ds))

if __name__=='__main__': main()
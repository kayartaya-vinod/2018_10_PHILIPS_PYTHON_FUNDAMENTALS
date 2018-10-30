'''
Exception handling using try-except block

Usage:
python ex10.py <num1> <num2>

Example:
python ex10.py 123 34
'''

import sys

def main():
    try: # try the following statements
        num = sys.argv[1]
        den = sys.argv[2]
        num, den = int(num), int(den)
        quo = num // den
        print('Quotient of {} divided by {} is {}'.format(num, den, quo))
    except: # handle any exception here
        print('OOPS! there was an error!')

    print('Thank you for using this script!')

if __name__=='__main__': main()
'''
Exception handling using try-except block

Usage:
python ex10.py <num1> <num2>

Example:
python ex10.py 123 34
'''

import sys

def main_1():
    try: # try the following statements
        num = sys.argv[1]
        den = sys.argv[2]
        num, den = int(num), int(den)
        quo = num // den
        print('Quotient of {} divided by {} is {}'.format(num, den, quo))
    except: # handle any exception here
        print('OOPS! there was an error!')

    print('Thank you for using this script!')


def main():
    try: # try the following statements
        num = sys.argv[1]
        den = sys.argv[2]
        num, den = int(num), int(den)
        quo = num // den
        print('Quotient of {} divided by {} is {}'.format(num, den, quo))
    except IndexError:
        print('You must supply two values')
    except ZeroDivisionError:
        print('Second number can not be zero')
        return
        # exit() # does not work in java
    except ValueError:
        print('Both inputs must be integers')
    except Exception as e:
        print('Something went wrong. This message may be of use - %s' % e)
    finally:
        print('Thank you for using this script!')

    print('**** end of main() ****')
if __name__=='__main__': main()
'''
This is an example of how to write a function
in Python and call/invoke the same
'''

def is_leap(year):
    if year % 400 == 0: return True
    
    if year % 4 == 0 and year % 100 != 0: return True 

    return False

def main():
    y = int(input('Enter an year number: '))
    if is_leap(y): 
        print('There are 366 days')
    else:
        print('There are 365 days')
    print('-'*70)

# In python, __name__ is the name of the module
# print('In ex03.py, __name__ is ', __name__)

if __name__ == '__main__':
    main()


'''
This is an example of while loop
'''

def print_table(num):
    print('Multiplication table for {}'.format(num))
    i = 1
    while i<=10:
        print('{} x {} = {}'.format(num, i, num*i))
        i += 1

print('id of print_table is: ' + str(id(print_table)))

# this function definition overrides the above function
def print_table(num):
    print('Multiplication table for {} :-'.format(num))
    i = 1
    while True:
        print('{} x {} = {}'.format(num, i, num*i))
        i += 1
        if i>10: break

print('id of print_table is: ' + str(id(print_table)))

def main():
    n = int(input('Enter a number: '))
    # functions are mere objects in Python,
    # they can be assigned to another variable, passed as 
    # function arguments and return from a function also
    pt = print_table
    pt(n)

if __name__ == '__main__':
    main()

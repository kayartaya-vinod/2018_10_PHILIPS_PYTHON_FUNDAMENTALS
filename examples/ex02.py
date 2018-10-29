"""
This module when executed will accept age of a person
and prints if he/she can vote or not!
"""

age = int(input('Enter your age: '))

if age >= 18:
    print('Yes, you can and must vote')
else:
    # print('Hey, you have to wait for another ' + str(18-age) + ' years')
    # print('Hey, you have to wait for another %d years' % (18-age))
    print('Hey, you have to wait for another {} years'.format(18-age))
    print('And after that don\'t forget to vote!')

print('End of the script execution')

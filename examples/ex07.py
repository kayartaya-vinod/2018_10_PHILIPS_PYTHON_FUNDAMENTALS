'''
This is an example of a 'for' loop.
The for loop should be used when we have a fixed iteration.
'''

def factorial(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f

def main():
    n = int(input('Enter a number: '))
    f = factorial(n)
    print('Factorial of %d is %d' % (n, f))


if __name__ == '__main__':
    main()
'''
This is an example of a recursive function.

Factorial of a number 'n' is f(n)
is nothing but n * f(n-1)
assuming factorial of n <=1 is 1
'''

def factorial(n):
    if n<=1: return 1
    return n * factorial(n-1)

def main():
    n = int(input('Enter a number: '))
    f = factorial(n)
    print('Factorial of %d is %d' % (n, f))

# invoke the main() only if run directly and not when imported
if __name__ == '__main__':
    main()


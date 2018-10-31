'''
Working with arbitrary arguments of function
'''

def average(*args):
    # print('type(args) is', type(args))
    # print('args contain', args)
    args = [a for a in args if type(a) in (int, float)]
    t = sum(args)
    c = len(args)
    return t/c

def main():
    avg  = average(10, 20, 40, 'asd', 495, 28, 484)
    print('average = ', avg)

if __name__=='__main__': main()
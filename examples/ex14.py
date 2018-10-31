'''
Working with keyword argument
'''

def fn1(n1, n2, *args, **kwargs):
    print('type(args) is', type(args))
    print('args contain', args)
    print('type(kwargs) is', type(kwargs))
    print('kwargs contain', kwargs)

def main():
    fn1(100, 200, 12, 34, 56, x=300, name='Vinod', email='vinod@vinod.co', phone='9731424784')

if __name__=='__main__': main()
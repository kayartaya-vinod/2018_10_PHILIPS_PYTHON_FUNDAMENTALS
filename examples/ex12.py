'''
Different types of function arguments
'''

# fn1 takes positional parameters
# city is a positional parameter with a default value
def fn1(name, email=None, city='Bangalore'):
    print('Name is: {}'.format(name))
    print('Email is: {}'.format(email))
    print('City is: {}'.format(city))
    print('-'*50)

def main():
    fn1('Vinod', 'vinod@vinod.co')
    fn1('John Doe', 'john@example.com', 'Dallas')
    fn1('Shyam', 'shyam@xmpl.com')
    # positional parameter can be used as a keyword argument
    fn1(email='krian.xmpl.com', name='Kiran')

    # members of the list/tuple will be passed as positional arguments
    data = ('Ravi', 'ravi@somecompany.com', 'Hassan')
    fn1(*data)

    data = {'name':'Shashi', 'email':'shashi@example.com', 'city': 'Udupi'}
    fn1(**data)
    # *data --> will pass the keys of the dict as positional args
    # **data --> will pass the values of the dict as positional args

if __name__=='__main__': main()
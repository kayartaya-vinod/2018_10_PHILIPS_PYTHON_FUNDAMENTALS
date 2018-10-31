'''
Using constructors for an object
'''

class Person:

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def print_info(self):
        print('Name  =', self.name)
        print('Email =', self.email)
        print()

def main():
    p1 = Person() 
    # call to 'Person()' is an instruction to Python to create an object
    # and invoke the Person.__init__ by supllying the reference of the 
    # newly created object, and then return the same reference, so that
    # it is assigned to 'p1'
    print('inside main(), id(p1) is', id(p1))
    # p1.__init__() # shouldn't be doing this
    p2 = Person('Vinod', 'vinod@vinod.co')
    # The arguments supplied are received by Python, and will further
    # be passed as additional parameters to __init__
    p1.print_info()
    p2.print_info()

if __name__=='__main__': main()
'''
Working with a class
'''

class Person:
    def info(self): # self is a reference to the invoking object
        print('information about this person...')
        print('id of self in info() is', id(self))
        # we can add new members to the object using 'self'
        self.fullname = ''
        self.email = ''
        self.age = ''
        print('-'*50)

def print_attributes(obj):
    print([at for at in dir(obj) if at.startswith('__')==False])

def main():
    p1 = Person() # creates an object and calls the constructor
    print('id of p1 in main() is', id(p1))
    print_attributes(p1)

    p1.info() # p1 is implicitly supplied as the first argument to info()
    print_attributes(p1)

    Person.info(p1) # invoking using a class like a static method

if __name__=='__main__': main()

'''
Using private variables and public properties
'''
class Person:

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.age = kwargs.get('age', None)

    # overriding the inherited (from object class) method
    def __str__(self):
        return '{} is {} years old.'.format(self.__name, self.__age)

    # readable property for the private __name
    @property
    def name(self):
        return self.__name

    # writable property 'name', which can assign value to __name
    @name.setter
    def name(self, value):
        if type(value) != str:
            raise TypeError('name must be string')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if type(value) not in (int, float):
            raise TypeError('age must be a number')
        if value<1 or value>120:
            raise ValueError('age must be between 1 and 120 years')

        self.__age = value

def main():
    p1 = Person(name='Krishna', age=50)
    p2 = Person(name='Harish', age=15)
    p1.age = 22     # try with non-numeric or outside range of 1-120

    print('p1.name is', p1.name)    # p1.name calls the @propert name
    p1.name = 'Krishna Kumar'       # p1.name = .. calls the @name.setter
    print('p1.name is', p1.name)

    # print(dir(p1))

    print(p1)
    print(p2.__str__())

    print('-'*50)
    # adds new attributes to p1
    p1.__name = 1230
    p1.__age = 'asdf'
    # print(dir(p1))

    print(p1)

if __name__=='__main__': main()
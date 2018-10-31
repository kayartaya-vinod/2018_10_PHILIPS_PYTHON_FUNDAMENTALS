'''
Using private variables and public properties
'''
class Person:

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.age = kwargs.get('age', None)

    # overriding the inherited (from object class) method
    def __str__(self):
        return 'Person [name={}, age={}]'.format(self.name, self.age)
        # return '{} is {} years old.'.format(self.__name, self.__age)

    # readable property for the private __name
    @property
    def name(self):
        return self.__name

    # writable property 'name', which can assign value to __name
    @name.setter
    def name(self, value):
        if value != None and type(value) != str:
            raise TypeError('name must be string')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value != None and type(value) not in (int, float):
            raise TypeError('age must be a number')
        if value != None and (value<1 or value>120):
            raise ValueError('age must be between 1 and 120 years')

        self.__age = value

    def __iadd__(self, value):
        if value==None: return self
        if type(value) in (int, float):
            self.age += value
        if type(value) == str:
            self.name += value
        return self

    def __lt__(self, value):
        if value!=None and type(value) in (int, float):
            return self.age < value
        if value!=None and type(value) == type(self):
            return self.age < value.age
        raise TypeError('Invalid type for < operator')

def main():
    p1 = Person(name='John', age = 22)
    p2 = Person(name='Miller', age = 24)

    if p1 < p2:     # executes p1.__lt__(p2)
        print('{} is younger than {}'.format(p1.name, p2.name))
    else:
        print('{} is older (or same age) than {}'.format(p1.name, p2.name))


def main_2():
    p1 = Person(name='James', age=30)
    print(p1)

    p1 += 5         # expect p1's age to be added with 5
    p1 += ' Bond'   # expect p1's name to be appended with ' Bond'
    print(p1)

def main_1():
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
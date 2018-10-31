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


class Employee(Person):

    def __init__(self, **kwargs):
        # super().__init__(**kwargs)
        Person.__init__(self, **kwargs)
        self.__id = kwargs.get('id')
        self.salary = kwargs.get('salary', 25000)

    @property
    def id(self): return self.__id

    @property
    def salary(self): return self.__salary

    # validation not done.
    @salary.setter
    def salary(self, value): self.__salary = value

    def __str__(self):
        return 'Employee [id={}, salary={}, {}]'.format(
            self.id, self.salary, Person.__str__(self))


def main():
    e1 = Employee(name='John', id=1010, age=33, salary=45000.0)
    print(e1)

if __name__=='__main__': main()
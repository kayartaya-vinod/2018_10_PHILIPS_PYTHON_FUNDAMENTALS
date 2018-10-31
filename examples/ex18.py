'''
Using inheritance in Python
'''

from ex17 import Person

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
    e1 = Employee(name='Ramesh', id=1212)
    print(e1)

if __name__=='__main__': main()
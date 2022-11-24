from Computer import *

class Employee:
    def __init__(self, computer):
        self.my_comp = computer


def try_simple():
    emp1 = Employee()
    comp = Computer()
    emp1.comp = comp
    print(emp1.comp.get_foo())
    print(emp1.comp.ram)

def complex():
    comp1 = Computer()
    print(comp1.ram)
    emp1 = Employee(comp1)

    print(emp1.my_comp.ram)

complex()

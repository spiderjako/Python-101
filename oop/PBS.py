class Soul:
    def __init__(self):
        print('Mental')
    def foo(self):
        return 2

class Body: 
    def __init__(self):
        print('Physically')
    def foo(self):
        return 42
class Person(Soul, Body):
    pass



print(Person.__mro__)
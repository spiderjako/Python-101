class Car:
    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed
    def __str__(self):
        return 'The car is a {0} {1} and its maximum speed is {2}'.format(self.car, self.model, self.max_speed)

class Driver(Car):
    def __init__(self, name, car):
        self.name = name
        super().__init__(car)
    def __str__(self):
        return 'The drivers name is {0} and he drives a {1}'.format(self.name, self.car)

a = Car('Bmw', 'e30', '200')
b = Driver('Carl', a)
print(str(a))

class Car:
    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed
    def __str__(self):
        return '{} {} with {} maximum speed.'.format(self.car, self.model, self.max_speed)

class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car
    def __str__(self):
        return '{} has a {}'.format(self.name, self.car)

def main():
    car_one = Car('BMW','e30','200')
    driver_one = Driver('Lyobcho',car_one)
    print(driver_one)
if __name__=='__main__':
    main()
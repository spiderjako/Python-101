class Worker:
    _hours = 8
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return "Worker's name is: {0}".format(self.name)

    def hours(self):
        return self._hours
    def get_min_salary(self):
        return self.min_salary()


class Tailor(Worker):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address
    def get_working_hours(self):
        return self.hours()

    @classmethod
    def calculate_hours(cls, hours_per_day):
        return hours_per_day * 3
    @classmethod
    def birthday_hours(cls, has_birthday = True):
        if has_birthday:
            return cls.calculate_hours(16)
        return 0

    @staticmethod
    def min_salary():
        return 580

t = Tailor('Dzuzepe', 'Sofia')
print(t.get_working_hours())
print(t.calculate_hours(12))
print(Tailor.calculate_hours(13))
print(t.min_salary())
print(Tailor.min_salary())
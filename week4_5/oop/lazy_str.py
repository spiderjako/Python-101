class Contract:
    def __init__(self, car, person, money):
        self.car = car
        self.person = person
        self.money = money

    @property
    def money(self):
        print('in property')
        return self.money * 1.95583
    @money.setter
    def money(self, value):
        print('in setter')
        self.money = value

    

contract_bmw = Contract('BMW', 'Jlyob4o', 20000)
print(contract_bmw.money)


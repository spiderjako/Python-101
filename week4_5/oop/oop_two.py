def sorting(lst):
    list(lst)
    i = 0
    j = 0 
    temp = 0
    while i < len(lst):
        j = 0
        while j < len(lst):
            if int(lst[i]) <= int(lst[j]):
                temp = lst[j]
                lst[j] =lst[i]
                lst[i] = temp
            j+=1
        i+=1
    return 


class Bill:
    def __init__(self, worth):
        self.worth = worth

    def __int__(self):
        return int(self.worth)

    def __str__(self):
        return "A {0}$ bill".format(self.worth)

    def __repr__(self):
        return str(self.worth)

    def __eq__(self, other):
        return self.worth == other.worth

    def __hash__(self):
        return hash((self.worth))

class BatchBill:
    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        return len(self.lst)

    def total(self):
        return sum(self.lst)

    def __getitem__(self, index):
        return self.lst[index]

class CashDesk:
    money = []

    def take_money(self, bills):
        if isinstance(bills, Bill):
            return self.money.append(bills)
        else:
            for i in bills:
                self.money.append(i)
    
    def total(self):
        summ = 0
        for i in self.money:
            summ += int(i)
        return summ

    

    def inspect(self):
        sorting(self.money)
        count = 1
        for i in range(len(self.money) - 1):
            if int(self.money[i]) == int(self.money[i+1]):
                count += 1
            else:
                print('{0}$ bills - {1}'.format(str(self.money[i]), count))
                count = 1
        if count>1:
            print('{0}$ bills - {1}'.format(str(self.money[i]), count))


def main():
    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]

    batch = BatchBill(bills)

    desk = CashDesk()

    desk.take_money(batch)
    print(desk.money)

    desk.take_money(Bill(10))
    print(desk.money)
    sorting(desk.money)
    print(desk.money)

    print(desk.total()) # 390
    desk.inspect()

if __name__ == '__main__':
    main()

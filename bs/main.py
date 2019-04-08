class Date:
    def __init__(self, day = 1, month = 1, year = 2000):
        self.day = day
        self.month = month
        self.year = year

    def _getDaysInMonth(self):
        if self.month in (4, 6, 9, 11):
            return 30
        elif self.month is 2:
            if self.isLeapYear():
                return 29
            return 28
        return 31

    def addDays(self, n):
        self.day += n
        while self.day > self._getDaysInMonth():
            self.day -= self._getDaysInMonth()
            self.month += 1
            if self.month is 13:
                self.month = 1
                self.year += 1

    def substrDays(self, n):
        self.day -= n
        while self.day < 1:
            self.month -= 1
            if self.month is 0:
                self.month = 12
                self.year -= 1
            self.day += self._getDaysInMonth()

    def isLeapYear(self):
        if self.year % 4 is 0 and self.year % 100 is not 0:
            return True
        elif self.year % 400 is 0:
            return True
        return False

    def getDaysTillChristmas(self):
        if self.month is 12:
            if self.day >= 25:
                days = 31 - self.day + 365
                if self.isLeapYear():
                    days += 1
            else:
                days = 25 - self.day
        else:
            month = self.month
            days = self._getDaysInMonth() - self.day
            self.month += 1
            while self.month != 12:
                days += self._getDaysInMonth()
                self.month += 1
            days += 25
            self.month = month
        return days

    def isLaterThen(self, date):
        if self.year > date.year:
            return True
        elif self.year is date.year:
            if self.month > date.month:
                return True
            if self.month is date.month and self.day > date.day:
                return True
        return False


def getDifference(date1, date2):
    if date1.year > date2.year:
        date = Date(date1.day, date1.month, date1.year - date2.year)
    else:
        date = Date(date2.day, date2.month, date2.year - date1.year)
    return date


if __name__ == '__main__':
    d1 = Date(31, 3, 2014)
    d2 = Date()

    d1.addDays(1)
    d2.substrDays(22)

    d3 = getDifference(d1, d2)

    print("Date3 is", d3.day, d3.month, d3.year)
    print("Date1 is leap year -", d1.isLeapYear())
    print("Date2 days till christmas -", d2.getDaysTillChristmas())
    print("Date1 is later then date2 -", d1.isLaterThen(d2))

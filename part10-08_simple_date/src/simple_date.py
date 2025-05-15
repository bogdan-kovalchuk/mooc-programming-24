class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    def __eq__(self, another):
        return self.__day == another.day and self.__month == another.month and self.__year == another.year

    def __ne__(self, another):
        return self.__day != another.day or self.__month != another.month or self.__year != another.year

    def __lt__(self, another):
        if self.__year < another.year:
            return True
        elif self.__year > another.year:
            return False
        else:
            if self.__month < another.month:
                return True
            elif self.__month > another.month:
                return False
            else:
                if self.__day < another.day:
                    return True
                else:
                    return False

    def __gt__(self, another):
        return not self.__lt__(another)

    def __add__(self, days):
        day = (self.__day + days) % 30
        month = (self.__month + (self.__day + days) // 30) % 12
        year = self.__year + (self.__month + (self.__day + days) // 30) // 12
        return SimpleDate(day, month, year)

    def __sub__(self, another):
        return abs((self.__year - another.year) * 360 + (self.__month - another.month) * 30 + self.__day - another.day)

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

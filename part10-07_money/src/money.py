class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __float__(self):
        return self.__euros + self.__cents / 100

    def __eq__(self, another):
        return float(self) == float(another)

    def __lt__(self, another):
        return float(self) < float(another)

    def __gt__(self, another):
        return float(self) > float(another)

    def __ne__(self, another):
        return float(self) != float(another)

    def __add__(self, another):
        amount = float(self) + float(another)
        euros = int(amount)
        cents = round((amount - euros) * 100)
        return Money(euros, cents)

    def __sub__(self, another):
        amount = float(self) - float(another)
        if amount < 0:
            raise ValueError(f"a negative result is not allowed")
        euros = int(amount)
        cents = round((amount - euros) * 100)
        return Money(euros, cents)

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"

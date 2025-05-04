class BankAccount:
    def __init__(self, owner_name: str, account_number: str, balance: float):
        self.__owner_name = owner_name
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, money):
        self.__balance += money
        self.__service_charge()

    def withdraw(self, money):
        self.__balance -= money
        self.__service_charge()

    def __service_charge(self):
        self.__balance -= 0.01 * self.__balance

    @property
    def balance(self):
        return self.__balance


if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)

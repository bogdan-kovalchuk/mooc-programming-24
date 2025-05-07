class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, weight: int):
        self.__weight = weight
        self.__current_weight = 0
        self.__items = []

    def add_item(self, item: Item):
        if self.__current_weight + item.weight() <= self.__weight:
            self.__current_weight += item.weight()
            self.__items.append(item)

    def print_items(self):
        for item in self.__items:
            print(item)

    def heaviest_item(self):
        return max(self.__items, key=lambda x: x.weight())

    def weight(self):
        return self.__current_weight

    def __str__(self):
        itm = "items"
        if len(self.__items) == 1:
            itm = "item"
        return f"{len(self.__items)} {itm} ({self.__current_weight} kg)"


class CargoHold:
    def __init__(self, weight):
        self.__weight = weight
        self.__current_weight = 0
        self.__suitcases = []

    def add_suitcase(self, suitcase: Suitcase):
        if self.__current_weight + suitcase.weight() <= self.__weight:
            self.__current_weight += suitcase.weight()
            self.__suitcases.append(suitcase)

    def __str__(self):
        suitcase = "suitcases"
        if len(self.__suitcases) == 1:
            suitcase = "suitcase"
        return f"{len(self.__suitcases)} {suitcase}, space for {self.__weight - self.__current_weight} kg"

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

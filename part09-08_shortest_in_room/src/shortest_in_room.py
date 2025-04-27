# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)
    
    def shortest(self):
        if not self.is_empty():
            return min(self.persons, key=lambda x: x.height)
        return None

    def remove_shortest(self):
        if not self.is_empty():
            return self.persons.pop(self.persons.index(self.shortest()))
        return None
        
    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        n_persons = len(self.persons)
        height = sum(person.height for person in self.persons)
        print(f"There are {n_persons} persons in the room, and their combined height is {height} cm")
        for person in self.persons:
            print(person) 


if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
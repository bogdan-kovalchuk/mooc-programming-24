class Task:
    task_id = 0

    def __init__(self, description, programmer, workload):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self._is_finished = False
        Task.task_id += 1
        self.id = Task.task_id

    def is_finished(self):
        return self._is_finished

    def mark_finished(self):
        self._is_finished = True

    def __str__(self):
        finished = {True: "FINISHED", False: "NOT FINISHED"}
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {finished[self._is_finished]}"


class OrderBook:
    def __init__(self):
        self.orders = []
        self.all_programmers = set()

    def add_order(self, description, programmer, workload):
        self.all_programmers.add(programmer)
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders

    def programmers(self):
        return list(self.all_programmers)


if __name__ == "__main__":
    print("##### Part 1 #####")
    t1 = Task("program hello world", "Eric", 3)
    print(t1.id, t1.description, t1.programmer, t1.workload)
    print(t1)
    print(t1.is_finished())
    t1.mark_finished()
    print(t1)
    print(t1.is_finished())
    t2 = Task("program webstore", "Adele", 10)
    t3 = Task("program mobile app for workload accounting", "Eric", 25)
    print(t2)
    print(t3)

    print("\n##### Part 2 #####")
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    for order in orders.all_orders():
        print(order)

    print()

    for programmer in orders.programmers():
        print(programmer)

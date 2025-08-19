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

    def mark_finished(self, id: int):
        for task in self.orders:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError(f"No task with id {id}")

    def unfinished_orders(self):
        return [task for task in self.orders if not task.is_finished()]

    def finished_orders(self):
        return [task for task in self.orders if task.is_finished()]

    def status_of_programmer(self, programmer):
        n_finished, n_unfinished, h_finished, h_unfinished = 0, 0, 0, 0
        is_presented = False
        for task in self.orders:
            if task.programmer == programmer:
                is_presented = True
                if task.is_finished():
                    n_finished += 1
                    h_finished += task.workload
                else:
                    n_unfinished += 1
                    h_unfinished += task.workload
        if not is_presented:
            raise ValueError("No programmer")
        return n_finished, n_unfinished, h_finished, h_unfinished


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

    print("\n##### Part 3 #####")
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    orders.mark_finished(1)
    orders.mark_finished(2)

    for order in orders.all_orders():
        print(order)

    print("\n##### Part 4 #####")
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)

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


class Application:
    def __init__(self):
        self.__oders = OrderBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        try:
            description = input("description: ")
            programmer, workload = input("programmer and workload estimate: ").split()
            workload = int(workload)
        except:
            print("erroneous input")
            return
        self.__oders.add_order(description, programmer, workload)
        print("added!")

    def finished_orders(self):
        finished_orders = self.__oders.finished_orders()
        if len(finished_orders) > 0:
            for task in finished_orders:
                print(task)
        else:
            print("no finished tasks")

    def unfinished_orders(self):
        unfinished_orders = self.__oders.unfinished_orders()
        if len(unfinished_orders) > 0:
            for task in unfinished_orders:
                print(task)
        else:
            print("no unfinished tasks")

    def mark_task_as_finished(self):
        try:
            self.__oders.mark_finished(int(input("id:")))
            print("marked as finished")
        except:
            print("erroneous input")
            return

    def programmers(self):
        print(self.__oders.programmers())

    def status(self):
        programmer = input("programmer: ")
        try:
            n_finished, n_unfinished, h_finished, h_unfinished = self.__oders.status_of_programmer(programmer)
        except:
            print("erroneous input")
            return

        print(
            f"tasks: finished {n_finished} not finished {n_unfinished}, hours: done {h_finished} scheduled {h_unfinished}"
        )

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":  # 0 exit
                break
            elif command == "1":  # 1 add order
                self.add_order()
            elif command == "2":  # 2 list finished tasks
                self.finished_orders()
            elif command == "3":  # 3 list unfinished tasks
                self.unfinished_orders()
            elif command == "4":  # 4 mark task as finished
                self.mark_task_as_finished()
            elif command == "5":  # 5 programmers
                self.programmers()
            elif command == "6":  # 6 status of programmer
                self.status()
            else:
                self.help()


Application().execute()

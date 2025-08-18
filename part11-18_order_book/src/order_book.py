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


if __name__ == "__main__":
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

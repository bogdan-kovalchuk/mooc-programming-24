class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    @property
    def credits(self):
        return self.__credits

    @property
    def grade(self):
        return self.__grade

    def __str__(self):
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"


class StudiesTracker:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: str, credits: str):
        if name in self.__courses and self.__courses[name].grade > grade:
            return
        self.__courses[name] = Course(name, grade, credits)

    def get_course(self, name: str):
        if not name in self.__courses:
            return None
        return self.__courses[name]

    def get_statistics(self):
        courses_number = len(self.__courses)
        credits = sum(course.credits for course in self.__courses.values())
        mean = sum(course.grade for course in self.__courses.values()) / courses_number
        grade_distr = [0, 0, 0, 0, 0, 0, 0]
        for course in self.__courses.values():
            grade_distr[course.grade] += 1
        return courses_number, credits, mean, grade_distr


class Application:
    def __init__(self):
        self.__studies_tracker = StudiesTracker()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__studies_tracker.add_course(course, grade, credits)

    def get_course(self):
        course_name = input("course: ")
        course = self.__studies_tracker.get_course(course_name)
        print(course) if course else print("no entry for this course")

    def statistics(self):
        courses_number, credits, mean, grade_distr = self.__studies_tracker.get_statistics()
        print(f"{courses_number} completed courses, a total of {credits} credits")
        print(f"mean {mean:.1f}")
        print("grade distribution")
        for i in range(5, 0, -1):
            print(f"{i}: {'x'*grade_distr[i]}")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course()
            elif command == "3":
                self.statistics()
            else:
                self.help()


Application().execute()

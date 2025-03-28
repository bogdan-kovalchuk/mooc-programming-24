def add_student(students: dict, student: str):
    if student not in students:
        students[student] = []


def add_course(students: dict, student: str, course: tuple):
    course_name = course[0]
    course_grade = course[1]
    if course_grade:
        student_course = next(
            (x for x in students[student] if x[0] == course_name), None
        )
        if student_course and student_course[1] < course_grade:
            students[student].remove(student_course)
            students[student].append(course)
        elif not student_course:
            students[student].append(course)


def average_grade(students: dict, student: str):
    return sum([x[1] for x in students[student]]) / len(students[student])


def print_student(students: dict, student: str):
    if student in students:
        print(f"{student}:")
        if len(students[student]):
            print(f" {len(students[student])} completed courses:")
            [print(f"  {course[0]} {course[1]}") for course in students[student]]
            print(f" average grade {average_grade(students, student):.1f}")
        else:
            print(" no completed courses")
    else:
        print(f"{student}: no such person in the database")


def summary(students: dict):
    if len(students):
        print(f"students {len(students)}")
        most_complited_courses = 0
        most_complited_courses_student = ""
        average_grade_st = 0
        best_average_grade_student = ""
        for student, courses in students.items():
            coml_courses = len(courses)
            average_grade_student = average_grade(students, student)
            if coml_courses > most_complited_courses:
                most_complited_courses = coml_courses
                most_complited_courses_student = student
            if average_grade_student > average_grade_st:
                average_grade_st = average_grade_student
                best_average_grade_student = student

        print(
            f"most courses completed {most_complited_courses} {most_complited_courses_student}"
        )
        print(f"best average grade {average_grade_st:.1f} {best_average_grade_student}")


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 1))
    add_course(students, "Peter", ("Software Development Methods", 5))
    print_student(students, "Peter")
    summary(students)

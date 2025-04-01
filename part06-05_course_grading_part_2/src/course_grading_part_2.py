st_info = input("Student information: ")
ex_compl = input("Exercises completed: ")
ex_points = input("Exam points: ")

students_info = {}
with open(st_info) as f_st_info:
    next(f_st_info)
    for line in f_st_info:
        info = line.strip().split(";")
        students_info[info[0]] = info[1] + " " + info[2]

exercises_points = {}
with open(ex_compl) as f_ex_compl:
    next(f_ex_compl)
    for line in f_ex_compl:
        compl = line.strip().split(";")
        exercises_points[compl[0]] = int(100 * (sum(map(int, compl[1:])) / 40) // 10)

exam_points = {}
with open(ex_points) as f_ex_points:
    next(f_ex_points)
    for line in f_ex_points:
        points = line.strip().split(";")
        exam_points[points[0]] = sum(map(int, points[1:]))

thresholds = [0, 15, 18, 21, 24, 28]
grades = [0, 1, 2, 3, 4, 5]
for id, nf in students_info.items():
    total_points = exercises_points[id] + exam_points[id]
    student_grade = [g for t, g in zip(thresholds, grades) if total_points >= t][-1]
    print(f"{nf} {student_grade}")

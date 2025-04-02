st_info = input("Student information: ")
ex_compl = input("Exercises completed: ")
ex_points = input("Exam points: ")

students_info = {}
with open(st_info) as f_st_info:
    next(f_st_info)
    for line in f_st_info:
        info = line.strip().split(";")
        students_info[info[0]] = info[1] + " " + info[2]

exercises_completed = {}
with open(ex_compl) as f_ex_compl:
    next(f_ex_compl)
    for line in f_ex_compl:
        compl = line.strip().split(";")
        exercises_completed[compl[0]] = sum(map(int, compl[1:]))

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

total_point = {}
student_grades = {}
thresholds = [0, 15, 18, 21, 24, 28]
grades = [0, 1, 2, 3, 4, 5]
for id, nf in students_info.items():
    total_points = exercises_points[id] + exam_points[id]
    total_point[id] = total_points
    student_grade = [g for t, g in zip(thresholds, grades) if total_points >= t][-1]
    student_grades[id] = student_grade

print(
    f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}"
)
for id, nf in students_info.items():
    print(
        f"{nf:30}{exercises_completed[id]:<10}{exercises_points[id]:<10}{exam_points[id]:<10}{total_point[id]:<10}{student_grades[id]:<10}"
    )

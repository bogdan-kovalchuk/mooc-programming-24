st_info = input("Student information: ")
ex_compl = input("Exercises completed: ")

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

for id, nf in students_info.items():
    print(f"{nf} {exercises_completed[id]}")

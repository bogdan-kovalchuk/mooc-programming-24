grades = [0] * 6
total_points = 0
students = 0
while user_input := input("Exam points and exercises completed: "):
    exam_points, exercises_completed = map(int, user_input.split())
    students += 1

    exercises_points = 0
    if 20 > exercises_completed >= 10:
        exercises_points = 1
    elif 30 > exercises_completed >= 20:
        exercises_points = 2
    elif 40 > exercises_completed >= 30:
        exercises_points = 3
    elif 50 > exercises_completed >= 40:
        exercises_points = 4
    elif 60 > exercises_completed >= 50:
        exercises_points = 5
    elif 70 > exercises_completed >= 60:
        exercises_points = 6
    elif 80 > exercises_completed >= 70:
        exercises_points = 7
    elif 90 > exercises_completed >= 80:
        exercises_points = 8
    elif 100 > exercises_completed >= 90:
        exercises_points = 9
    elif exercises_completed == 100:
        exercises_points = 10

    total_exam_points = exam_points + exercises_points
    total_points += total_exam_points

    if exam_points < 10 or 14 >= total_exam_points >= 0:
        grades[0] += 1
    elif 17 >= total_exam_points >= 15:
        grades[1] += 1
    elif 20 >= total_exam_points >= 18:
        grades[2] += 1
    elif 23 >= total_exam_points >= 21:
        grades[3] += 1
    elif 27 >= total_exam_points >= 24:
        grades[4] += 1
    elif 30 >= total_exam_points >= 28:
        grades[5] += 1


print("Statistics:")

points_average = total_points / students
print(f"Points average: {points_average:.1f}")

pass_percentage = 100 * (sum(grades) - grades[0]) / sum(grades)
print(f"Pass percentage: {pass_percentage:.1f}")

print("Grade distribution:")
for i in range(len(grades) - 1, -1, -1):
    print(f"{i}: {'*' * grades[i]}")

# Write your solution here
course_student_count = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))

num_groups = course_student_count // group_size
if course_student_count % group_size != 0:
    num_groups += 1
    
print(f"Number of groups formed: {num_groups}")
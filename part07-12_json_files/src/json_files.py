import json


def print_persons(filename: str):
    with open(filename, encoding="utf-8") as f:
        students = json.load(f)

    for student in students:
        name = student.get("name", "Unknown")
        age = student.get("age", "N/A")
        hobbies = ", ".join(student.get("hobbies", []))
        print(f"{name} {age} years ({hobbies})")

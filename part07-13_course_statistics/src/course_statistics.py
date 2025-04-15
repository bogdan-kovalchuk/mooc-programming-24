import urllib.request
import json
import math


def retrieve_all():
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    response = urllib.request.urlopen(url)
    courses = json.load(response)
    return [
        (course["fullName"], course["name"], course["year"], sum(course["exercises"]))
        for course in courses
        if course["enabled"]
    ]


def retrieve_course(course_name: str):
    course_url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    response = urllib.request.urlopen(course_url)
    data = json.load(response)

    return {
        "weeks": len(data),
        "students": max(c["students"] for _, c in data.items()),
        "hours": sum(c["hour_total"] for _, c in data.items()),
        "hours_average": math.floor(
            sum(c["hour_total"] for _, c in data.items()) / max(c["students"] for _, c in data.items())
        ),
        "exercises": sum(c["exercise_total"] for _, c in data.items()),
        "exercises_average": math.floor(
            sum(c["exercise_total"] for _, c in data.items()) / max(c["students"] for _, c in data.items())
        ),
    }

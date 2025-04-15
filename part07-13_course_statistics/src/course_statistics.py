import urllib.request
import json


def retrieve_all():
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    with urllib.request.urlopen(url) as response:
        courses = json.load(response)

    return [(course["fullName"], course["name"], course["year"], sum(course["exercises"])) for course in courses]


print(retrieve_all())

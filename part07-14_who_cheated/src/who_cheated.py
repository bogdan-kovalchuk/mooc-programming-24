from datetime import time


def convert_to_min(t: str):
    h, m = map(int, t.split(":"))
    return 60 * h + m


def cheaters():
    with open("start_times.csv") as start_times_file, open("submissions.csv") as submissions_file:
        students = {n: convert_to_min(t) for n, t in (line.strip().split(";") for line in start_times_file)}

        failed_students = set()
        for line in submissions_file:
            name, _, _, passed_time = line.strip().split(";")
            submission_time = convert_to_min(passed_time)
            if submission_time - students[name] > 180:
                failed_students.add(name)
        return sorted(failed_students)

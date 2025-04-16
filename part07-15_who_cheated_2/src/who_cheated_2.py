from datetime import time


def convert_to_min(t: str):
    h, m = map(int, t.split(":"))
    return 60 * h + m


def final_points():
    with open("start_times.csv") as start_times_file, open("submissions.csv") as submissions_file:
        start_time = {n: convert_to_min(t) for n, t in (line.strip().split(";") for line in start_times_file)}
        final_exam_points = dict()
        for line in submissions_file:
            name, task, points, passed_time = line.strip().split(";")
            submission_time = convert_to_min(passed_time)
            if submission_time - start_time[name] > 180:
                continue
            if name not in final_exam_points:
                final_exam_points[name] = {task: int(points)}
            elif task not in final_exam_points[name]:
                final_exam_points[name].update({task: int(points)})
            elif int(points) > final_exam_points[name][task]:
                final_exam_points[name][task] = int(points)

        for name, vals in final_exam_points.items():
            final_exam_points[name] = sum(v for n, v in vals.items())

        return final_exam_points

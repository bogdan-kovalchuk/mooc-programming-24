import datetime

filename = input("Filename: ")
day, month, year = map(int, input("Starting date: ").split("."))
days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")
start_day = datetime.datetime(year, month, day)
last_day = None
screen_time = []
for i in range(days):
    d = (start_day + datetime.timedelta(days=i)).strftime("%d.%m.%Y")
    screen_time.append((d, list(map(int, input(f"Screen time {d}: ").split()))))

with open(filename, "w") as f:
    f.write(f"Time period: {screen_time[0][0]}-{screen_time[-1][0]}\n")
    total_min = sum(sum(e[1]) for e in screen_time)
    f.write(f"Total minutes: {total_min}\n")
    average_min = total_min / days
    f.write(f"Average minutes: {average_min:.1f}\n")
    for day, times in screen_time:
        t1, t2, t3 = times
        f.write(f"{day}: {str(t1)}/{str(t2)}/{str(t3)}\n")
    print(f"Data stored in {filename}")

year = int(input("Year:"))
leap_year = year + 1

while True:
    if (leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0):
        print(f"The next leap year after {year} is {leap_year}")
        break
    leap_year += 1

    
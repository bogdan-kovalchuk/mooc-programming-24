file_name = "diary.txt"
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = input("Function:")
    if function == "1":
        entry = input("Diary entry:")
        with open(file_name, "a") as f:
            f.write(entry + "\n")
        print("Diary saved")
    elif function == "2":
        print("Entries:")
        with open(file_name) as f:
            for line in f:
                print(line.rstrip())
    elif function == "0":
        print("Bye now!")
        break

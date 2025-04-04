def store_personal_data(person: tuple):
    with open("people.csv", "a") as f:
        f.write(";".join(map(str, person)))

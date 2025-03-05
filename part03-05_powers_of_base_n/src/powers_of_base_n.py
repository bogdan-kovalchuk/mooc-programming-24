limit = int(input("Upper limit:"))
base = int(input("Base:"))

num_to_print = 1
while num_to_print <= limit:
    print(num_to_print)
    num_to_print *= base

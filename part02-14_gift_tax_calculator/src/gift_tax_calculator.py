value_of_gift = int(input("Value of gift:"))

if 5000 <= value_of_gift < 25000:
    tax_amount = 100 + (value_of_gift - 5000)*0.08
elif 25000 <= value_of_gift < 55000:
    tax_amount = 1700 + (value_of_gift - 25000)*0.1
elif 55000 <= value_of_gift < 200000:
    tax_amount = 4700 + (value_of_gift - 55000)*0.12
elif 200000 <= value_of_gift < 1000000:
    tax_amount = 22100 + (value_of_gift - 200000)*0.15
elif value_of_gift >= 1000000:
    tax_amount = 142100 + (value_of_gift - 1000000)*0.17

if value_of_gift < 5000:
    print("No tax!")
else:
    print(f"Amount of tax: {tax_amount} euros")

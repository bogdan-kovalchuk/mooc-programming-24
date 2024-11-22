pin = "4321"

attemps = 0
while True:
    entered_pin = input("PIN:")
    attemps += 1
    if pin == entered_pin:
        if attemps == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attemps} attempts")
        break
    else:
        print("Wrong")


    
points = int(input("How many points [0-100]:"))

if points < 0:
	print("impossible!")
elif 0 <= points <= 49:
    print("Grade: fail")
elif 50 <= points <= 59:
	print("Grade: 1")
elif 60 <= points <= 69:	
    print("Grade: 2")
elif 70 <= points <= 79:	
    print("Grade: 3")
elif 80 <= points <= 89:	
    print("Grade: 4")
elif 90 <= points <= 100:	
    print("Grade: 5")
else: 
    print("impossible!")
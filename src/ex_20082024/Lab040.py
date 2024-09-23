score=int(input("Enter your score\n"))
if 90 <= score <= 100:
    print("Your grade is", "A")
elif 80 <= score <= 89:
    print("Your grade is", "B")
elif 70 <= score <= 79:
    print("Your grade is", "C")
elif 60 <= score <= 69:
    print("Your grade is", "D")
else:
    print("Failed","F")

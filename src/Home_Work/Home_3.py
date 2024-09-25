#Task 6


year=(input("Enter the year\n"))
year=int(year)
if (year % 4 == 0) and (year % 100 != 0) or(year % 400 == 0):
    print("This is a Leap year")
else:
    print("This is not a Leap year")


# task 7

a=int(input("Enter the sides\n"))
b=int(input("Enter the sides\n"))
c=int(input("Enter the sides\n"))
print(a)
print(b)
print(c)
if a== b== c:
    print("Its a equilateral triangle")
elif a == b!=c:
    print("Its a isosceles triangle")
else:
    print ("Its a Scalene triangle")


# Task 8

for i in range(1, 101):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif (i%3==0) and (i%5==0):
        print("FizzBuzz")
    else:
        print(i)


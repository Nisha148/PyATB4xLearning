try:
    a = int(input("Enter the num1"))
    b = int(input("Enter the num2"))
    result= a / b
except ZeroDivisionError as zde:
    print("Zero div error, Don't use the Num2 as 0")
except ValueError as ve:
    print("Value error,You have entered the string instead we want int")
else:
    print(f"result  {result}")
finally:
    print("This code is always executed")
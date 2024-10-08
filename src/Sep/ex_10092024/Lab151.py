print("---Start of the program---")
try:
    a = int(input("Enter the num1"))
    b = int(input("Enter the num2"))
    c = a / b
    print("Result  ", c)
except Exception as e:
    print(e)
    print("Please check your inputs,it should't be a string or zero")

print("---end of the program---")
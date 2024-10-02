# Task 9

num = int(input("Enter the number"))
print(num)
fact = 1
for i in range(1, num + 1, 1):
    fact = fact * i
print(fact)

n = int(input("Enter Number: "))
a = 0
b = 1
print(a, b, end=" ")
for i in range(0, n+1):
    c = a + b
    print(c, end=" ")
    a = b
    b = c

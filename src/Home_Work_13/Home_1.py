"""Task #1
# Home Can you create a Program I will give you number(userinput and print table)
f"{}" String format concept
User input - num int -> 10, 100, -1, 2, 3.14 -> input
9x1 = 9
9x2 = 18... till 10
"""

#Task1

tables=9
print(f"{tables}*1={tables*1}")
print(f"{tables}*2={tables*2}")
print(f"{tables}*3={tables*3}")
print(f"{tables}*4={tables*4}")
print(f"{tables}*5={tables*5}")
print(f"{tables}*6={tables*6}")
print(f"{tables}*7={tables*7}")
print(f"{tables}*8={tables*8}")
print(f"{tables}*9={tables*9}")
print(f"{tables}*10={tables*10}")

#Task #2

#Create a program , take 2 inputs from the user num1, num2 and give them
#max
#pow num1 to num2
#sub, mul, sum, div.
#Format your out with f{""}

number1=int(input("Enter the number1"))
number2=int(input("Enter the number2"))
print(f"Maximum number={max(number1,number2)}")
print(f"Power={pow(number1,number2)}")
print(f"Sub={number1-number2}")
print(f"Mul={number1*number2}")
print(f"sum={number1+number2}")
print(f"Div={number1/number2}")

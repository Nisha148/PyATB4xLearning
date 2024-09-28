def find_even_odd(num):
    if num %2==0:
        print("Even")
    else:
        print("odd")

find_even_odd(5)


find_even_odd1=lambda num:"Even" if num%2==0 else "odd"
print(find_even_odd1(11))
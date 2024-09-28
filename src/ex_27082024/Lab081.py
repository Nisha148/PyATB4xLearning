def triple_me(num):
    return num*3

o=triple_me(10)
print(o)

def triple_me(num):
    return num**3

o=triple_me(10)
print(o)

o=lambda num:num ** 3
print(o(10))
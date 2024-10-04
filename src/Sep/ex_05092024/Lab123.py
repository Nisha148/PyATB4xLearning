class Myclass:

    public_var="I Am Public"
    balance=100

    __private_var="I AM PRIVATE"
    __password="123"

    _protected_var="I AM PROTECTED"


object=Myclass()
print(object.public_var)
print(object._protected_var)
print(object.balance)
class MyCustomException(Exception):

    def __init__(self,message):
        self.message=message
        super().__init__(message)

balance=100
withdraw=int(input("enter the amount\n"))
if withdraw>=balance:
    raise MyCustomException("Balance is too Low!!")
else:
    print("Remaining Balance ",(balance-withdraw))
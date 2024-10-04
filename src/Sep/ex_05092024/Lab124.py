class Bank:

    def __init__(self,account_number,balance):
        self.balance=balance
        self.__account_number=account_number

    def deposite(self,amount):
        self.balance=self.balance+amount

    def check_balance(self):
        print(self.balance)

    def show_me_the_account_number(self,is_auth):
        if is_auth==True:
            print(self.__account_number)
        else:
            print("Not Allowed!")

output=Bank(1234567,100)
output.deposite(100)
output.check_balance()
output.show_me_the_account_number(False)
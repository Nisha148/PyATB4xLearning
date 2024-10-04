class VWOLoginPage:

    def __init__(self,email_arg,password_arg):
        self.email=email_arg
        self.password=password_arg

    def login_conf(self):
        if self.email=="pramod@gmail.com" and self.password=="Pass123":
            print("Login successfull")
        else:
            print("Error")


email=input("Enter the email\n")
password=input("Enter the password\n")
vwo_obj=VWOLoginPage(email,password)
vwo_obj.login_conf()
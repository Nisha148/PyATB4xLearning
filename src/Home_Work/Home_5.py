from tkinter.font import names


class Employee:
    name=None
    age=None
    phone=None
    address=None
    eid=None

    def __init__(self,name,age,phone,address,eid):
        print("Employers details")
        self.name=name
        self.age=age
        self.phone=phone
        self.address=address
        self.eid=eid


    def employers_details(self):
        print("Employers name= ",self.name)
        print("Employers age= ",self.age)
        print("Employers phone= ",self.phone)
        print("Employers address= ",self.address)
        print("Employers eid= ",self.eid)
        return None


name=input("Enter the employer name\n")
age=input("Enter the employer age\n")
phone=input("Enter the employer phone\n")
address=input("Enter the employer address\n")
eid=input("Enter the employer eid\n")
Employer_1=Employee(name,age,phone,address,eid)
Employer_1.employers_details()


name=input("Enter the employer name\n")
age=input("Enter the employer age\n")
phone=input("Enter the employer phone\n")
address=input("Enter the employer address\n")
eid=input("Enter the employer eid\n")
Employer_2=Employee(name,age,phone,address,eid)
Employer_2.employers_details()
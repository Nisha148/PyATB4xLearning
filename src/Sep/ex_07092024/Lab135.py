class GrandFather:
    x=10

    def home(self):
        print("Old Home")

class Father(GrandFather):
    a=30

    def home(self):
        print("1BHK")
        print(self.a)
        print(super().x)

class Son(Father):
    b=20

    def home(self):
        super().home()
        print(super().a)
        print("No House")
        print(self.b)

s=Son()
s.home()
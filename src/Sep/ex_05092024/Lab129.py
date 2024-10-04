class Father:

    def father_money(self):
        return 5
    def home(self):
        return "Father"

class Mother:

    def mother_money(self):
        return 2

    def home(self):
        return "Mother"

class Son(Mother,Father):
    pass

s=Son()
print(s.father_money())
print(s.mother_money())
print(s.home())
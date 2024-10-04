class father:

    def bhk1(self):
        print("1BHK")

class pramod(father):

    def bhk2(self):
        print("2BHK")

class Amith(father):

    def bhk3(self):
        print("3BHK")

class Lucky(father):

    def no_house(self):
        print("No House")

p=pramod()
p.bhk1()
p.bhk2()

a=Amith()
a.bhk3()
a.bhk1()

l=Lucky()
l.bhk1()
l.no_house()

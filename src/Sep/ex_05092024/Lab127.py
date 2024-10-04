class Parent:
    gold="2Kg"

    def BHK2(self):
        print("BHK2")

class Child(Parent):

    def BHK3(self):
        print("3BHK")

child_ob=Child()
child_ob.BHK3()
child_ob.BHK2()
print(child_ob.gold)

father_ob=Parent()
father_ob.BHK2()
#father_ob.BHK3()
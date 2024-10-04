class Father:
    key="3BHK"

    def car(self):
        print("Father car!!",self.key)

class son(Father):
    key2="3BHK"

    def home(self):
        print(self.key2)

    def truck(self):
        print("Truck")

father_object=Father()
father_object.car()

son_obj=son()
son_obj.home()
son_obj.truck()
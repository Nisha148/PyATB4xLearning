class Dog:
    name = None

    def __init__(self,name):
        print("Automatically Called")
        self.name=name

    def sleep(self):
        print("Sleeping")


dog1 = Dog("chow")
print(dog1.name)

dog2 = Dog("mow")
print(dog2.name)


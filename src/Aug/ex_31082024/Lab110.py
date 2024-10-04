class Dog:
    name = None

    def __init__(self):
        print("Automatically Called")

    def sleep(self):
        print("Sleeping")


dog1 = Dog()
dog1.sleep()
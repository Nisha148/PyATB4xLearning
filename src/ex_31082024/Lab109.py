from time import perf_counter_ns


class Dog:
    name=None
    breed=None
    Color=None

    def sleep(self):
        print("Sleeping")

    def bark(self):
        print("bark")

    def eat(self):
        print("food")

dog1=Dog()
print(dog1.name)
dog1.name="Chow"
print(dog1.name)
dog1.sleep()

print("--------------------------------")

dog2=Dog()
print(dog2.name)
dog2.name="Mow"
print(dog2.name)
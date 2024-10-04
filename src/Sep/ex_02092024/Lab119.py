class person:

    def __init__(self,name):
        self.name=name

    def walk(self):
        print(self.name)

amit=person("Amit")
pramod=person("Pramod")
print(amit.name)
print(pramod.name)
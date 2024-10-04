


class car:

    def __init__(self,o_name,o_make,o_model):
        self.name=o_name
        self.make=o_make
        self.model=o_model

    def start_engine(self):
        print("Start a car with the name ",self.name)
        print("Start a car with the make ",self.make)
        print("Start a car with the model ",self.model)

Lambo=car("Lambo","V2","2024")
Lambo.start_engine()

XUV=car("xuv","V6","2023")
XUV.start_engine()


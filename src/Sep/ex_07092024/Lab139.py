from abc import ABC,abstractmethod


class Gearbox(ABC):

    @abstractmethod
    def setup_Gearbox(self):
        pass

class Engine:

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        pass

class Car(Engine):

    def start(self):
        print("Start")

    def setup_Gearbox(self):
        print("Gearbox is ready")

    def stop(self):
        print("Stop")

    def drive(self):
        self.start()
        self.setup_Gearbox()
        self.stop()

car=Car()
car.drive()

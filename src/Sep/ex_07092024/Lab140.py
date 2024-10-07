from abc import ABC,abstractmethod


class Excel(ABC):

    @abstractmethod
    def readfromExcel(self):
        pass

class Browser(Excel):

    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass

class TC1(Browser):

    def startBrowser(self):
        print("Start")

    def stopBrowser(self):
        print("Stop")

    def readfromExcel(self):
        print("Readfrom Excel is ready")

    def runTC(self):
        self.startBrowser()
        self.readfromExcel()
        self.stopBrowser()

tc1=TC1()
tc1.runTC()
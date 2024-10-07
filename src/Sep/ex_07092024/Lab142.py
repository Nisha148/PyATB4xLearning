class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from Excel")

class TC1:

    def runTc(self):
        ExcelReader.readExcelFile()

tc=TC1()
tc.runTc()
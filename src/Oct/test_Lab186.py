import pandas as pd

class Test_CRUD(object):
    def test_update_2(self):
        df=pd.read_csv("src/Oct/userdata.csv")
        print(df)
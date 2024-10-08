class XYZ:

    def f1(self):
        try:
            a=int(input("Enter the value of a\n"))
        except Exception as e:
            print("enter int only value of a ")
        else:
            print(a)
        finally:
            print("FINALLY: Anyhow i will be printed")

xyz=XYZ()
print(xyz.f1())
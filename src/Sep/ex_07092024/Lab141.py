


class O:

    @staticmethod
    def sum(a,b):
        return a+b

class MathOperation(O):

    def div(self,a,b):
        return a/b

    def mul(self,a,b):
        return a*b

    @staticmethod
    def sum(a,b):
        return a+b

    @staticmethod
    def sub(a,b):
        return a-b

object_ref1=MathOperation()
output1=object_ref1.div(10,5)
output2=object_ref1.mul(10,5)
print(output1)
print(output2)

print(MathOperation.sum(4,5))
print(MathOperation.sub(4,5))
print(O.sum(5,4))
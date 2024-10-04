class A:

    def methodA(self):
        return "A"

class B(A):

    def methodB(self):
        return "B"

class c(A):

    def methodC(self):
        return "C"

class D(B,c):

    def methodD(self):
        return "D"

d=D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())
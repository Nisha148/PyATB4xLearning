class GrandFather:
    gold="2KG"

    def bhk1(self):
        print("1BHK")

class Father(GrandFather):
    diamond="22 Karat"

    def bhk2(self):
        print("2BHK")

class Son(Father):
    btc="1 BTC"

    def bhk3(self):
        print("3BHK")

s=Son()
print(s.gold)
print(s.diamond)
s.bhk1()
s.bhk2()
s.bhk3()

f=Father()
print(f.diamond)
print(f.gold)
f.bhk2()
f.bhk1()

g=GrandFather()
print(g.gold)
g.bhk1()
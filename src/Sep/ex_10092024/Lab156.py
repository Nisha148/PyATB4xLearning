import os

print(os.name)
if os.name=="Posix":
    print("mac")
else:
    print("Windows")
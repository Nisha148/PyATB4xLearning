a=10

class person:
    b = 11

    def print_info(self):
       global a
       a="Hello"
       print(self.b)

output_print=person()
output_print.print_info()
print(a)
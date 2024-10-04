def say_hello_default_arg(name="pramod"):
    print("Hello,",name)

say_hello_default_arg("Amit")
say_hello_default_arg()
say_hello_default_arg(name="Tushar")


def multiple_args(name1,name2,name3):
    print("Multiple Arguments, ",name1,name2,name3)

multiple_args(name1="Ram",name2="Yunus",name3="Deeps")
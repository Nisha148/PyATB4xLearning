def print_arguments(*args):
    print(args[0])

    print_arguments("pramod", "amit", "lucky")
    print_arguments("amit", "lucky")
    print_arguments("amit", 10)
    print_arguments("amit", 10, True)
    print_arguments("amit", 10, True, False)
    print_arguments("lucky")

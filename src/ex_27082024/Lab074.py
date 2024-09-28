def my_decorator(fun):
    def wrapper():
        print("Before the function is called")
        print("Add Helmet,Dashcam,Gloves,Knee guards")
        fun()
        print("After the function is called")
        print("Secure driving")
    return wrapper()


@my_decorator
def drive_bike():
    print("I am driving")

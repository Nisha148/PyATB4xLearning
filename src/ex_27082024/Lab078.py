import time


def decorator_time(func):

    def wrapper():
        start_time=time.time()
        print(start_time)
        func()
        end_time=time.time()
        print(end_time)
        print(f"Time Taken= {end_time-start_time}")

    return wrapper()


@decorator_time
def test_ui_1():
    print("Add a function,time taken by this function")
    time.sleep(2)


@decorator_time
def test_ui_2():
    print("Add a function,time taken by this function")
    time.sleep(5)



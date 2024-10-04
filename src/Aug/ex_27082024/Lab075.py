def add_before_ui_after_ui(fun):
    def wrapper():
        print("Before the running UI Tc")
        print("Start the browser")
        fun()
        print("Ending the running UI TC")
        print("Quit the browser")
    return wrapper()


@add_before_ui_after_ui
def test_ui():
    print("I will test the UI")

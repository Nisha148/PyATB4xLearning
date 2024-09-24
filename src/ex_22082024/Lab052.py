browser_name=input("Enter the browser name\n")
browser_name=browser_name.lower()
match browser_name:
    case"Firefox":
        print("execute the firefox code")
    case "Chrome":
        print("execute the Chrome code")
    case "Edge":
        print("execute the Edge code")
    case "safari":
        print("execute the safari code")
    case _:
        print("Browser not Found!")
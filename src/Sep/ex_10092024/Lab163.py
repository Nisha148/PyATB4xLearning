try:
    with open("testdata,txt", "r") as file:
        content = file.readlines()
        print(content)
except FileNotFoundError as fnfe:
    print("FNFE")
finally:
    try:
        file.close()
    except NameError as ne:
        print("NE")
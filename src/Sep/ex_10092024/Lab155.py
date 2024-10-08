try:
    file=open("testdata.txt","r")
    print(file.read())
except FileNotFoundError as fne:
    print("File not found, please fix the file or create a file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)
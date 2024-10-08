import os

#print(os.getcwd())
#os.chdir("/Users/nisan/Downloads")
#print(os.getcwd())

#os.mkdir("new_directory")

#os.makedirs("parent/child/grandchild")

#print(os.listdir("."))
#for file in os.listdir("."):
 #   print(file)


#os.remove("example.txt")

#os.rmdir("new_directory")

#os.rename("old_file.txt","new_file.txt")

full_path=os.path.join("C:/Users/nisan/PycharmProjects/PyATB4xLearning/src/Sep/ex_10092024","file.txt")
print(full_path)
print(os.path.exists("file.txt"))

print(os.path.isfile("file.txt"))

print(os.path.isdir("directory_name"))
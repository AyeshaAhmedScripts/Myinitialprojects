import os

path = "C:\\Users\\sohai\\OneDrive\\Desktop\\text"

if os.path.exists(path):
    print("That location exist!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist!")
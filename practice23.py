import os

path =("test.txt")


try:
    os.remove(path)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You need permission")
else:
    print(path + " was deleted")
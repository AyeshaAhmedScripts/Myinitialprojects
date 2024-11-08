import os
source = "lyrics.txt"
destination ="C:\\Users\\sohai\\OneDrive\\Desktop\\lyrics.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print (source + " was moved")
except FileNotFoundError:
        print((source+ " was not found"))

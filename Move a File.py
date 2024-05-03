import os

source = "copy.txt"
destination = "C:\\Users\\hfsha\\OneDrive\\Documents\\copy.txt"

try:
    if os.path.exists("C:\\Users\\hfsha\\OneDrive\\Documents\\copy.txt"):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")
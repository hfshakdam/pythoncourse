try:
    with open("C:\\Users\\hfsha\\OneDrive\\Documents\\test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
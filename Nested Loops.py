#Just a loop inside of a loop

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("What symbol?: ")

for i in range(rows): #the i and j are not important, can be any letter
    for j in range(columns):
        print(symbol, end="")
    print()
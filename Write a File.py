text = ("This is the overwritten text from the IDE\n"
        "the backslash and n make this a new line")

with open ("C:\\Users\\hfsha\\OneDrive\\Documents\\test.txt", 'w') as file:
    file.write(text)
# the second argument is default to R for read. You can make it W for write

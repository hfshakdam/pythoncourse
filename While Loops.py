#While loops = a statement that will exectute it's block of code
#               as long as it's condition remains true

#while 1==1:#1 is always going to be equal to 1
 #   print("Help, i'm stuck in a loop!")

name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello "+name)
# str.format() = optional method that gives users
#                more control when displaying output


animal = "cow"
item = "moon"

#print("The {} jumped over the {}!".format(animal,item))
#print("The {1} jumped over the {0}!".format(animal,item)) #postional argument (flips it)
#print("The {animal} jumped over the {item}!".format(animal="cow",item="moon")) #keyword argument

text = "The {} jumped over the {}!"
print(text.format(animal,item))
#the above is an elegenat way to write this code

name = "Hisham"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}, *testing space*".format(name))
#the {:10} provides 10 spaces after the variable

number = 3.14159

print("The number pi is {:.2f}".format(number))
#f is for floating point number
#the 2 shows how many digits after the decimal will be displayed
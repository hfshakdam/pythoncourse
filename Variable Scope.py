#scope = the region that a variable is recognised
#a variable is only available from inside the region it is created
#a global and locally scoped versions of a variable can be created

#local variables are prioritised

name = "Silver" #a global variable avaible in and out of functions

def display_name():
    name = "Garnet"
    print(name) #"name" is not defined outside of the function. Local scope.

display_name()
print(name)


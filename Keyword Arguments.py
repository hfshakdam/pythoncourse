#arguments that are preceded by an indentifier when we pass them to a function
#   The order of the arguments doesn't matter, unlike positional arguments
#   Python knows the names of the arguments that our function recieves

def hello(first, middle, last): #def is "defining the function"
   print("Hello "+first+" "+middle+" "+last)

#hello("Hisham","Silver","Shakdam") #This is positional and will print in this order only

hello(last="Shakdam",middle="Silver",first="Hisham")
#this can be out of order and print based on the orignal function's order because we
#assigned arguments to it
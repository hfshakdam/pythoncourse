#nested function calls = function calls inside other function calls
#innermost funnction calls are resolved first
#returned value is used as argument for the next outer function
#Sort of similar to BIDMAS

#num = input("Enter a whole positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

#the above can be written much shorter using nested function calls like so:

print(round(abs(float(input("Enter a whole positive number: ")))))
# exception = events deteceted during execution that interrupts the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e) #additional and optional way to handle exceptions
    print("You can't divide by zero")
except ValueError as e:
    print(e) #prints the error type
    print("Enter only numbers pls")
#except Exception:#except blocks on their own like this aren't good practice
    # Better to handle excpetions individually
 #   print("Something went wrong")
else:
    print(result)
finally:
    print("this will always execute")

#Using the "try" block is useful when code is considered dangerous
#dangerous code = code that is prone to exceptions
#code that requires user input is dangerous because you don't know what they'll input
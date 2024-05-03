#list = Store multiple items in a single variable
# each item in a lsit is refered to as an element

food = ["pizza", "pasta", "bread"]
#pizza is element "0" in the list
food[0] = "sushi" #you can change list elements whenever

#print(food[0])

food.append("ice-cream") #add ice-cream to the end of the list
food.remove("pasta") #removes pasta from the list
food.pop() #removes the last element
food.insert(0,"cake") #moves the lsit forward and element 0 becomes cake
food.sort() #sorts alphabetically
food.clear()#removes all elements

for i in food: #"for the index in food"
    print(i, end=" ")
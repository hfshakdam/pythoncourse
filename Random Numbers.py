import random
#importing a module called "random"

#x = random.randint(1,10) #will give me random numbers between 1 and 10
#y = random.random() #prints random floats between 0 and 1
#print(y)

player1 = ['rock','paper','scissors']
z = random.choice(player1)
print(z)

cards = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
random.shuffle(cards)

print(cards)



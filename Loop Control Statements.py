#loop control statements = change a loops execution from its normal sequence

#break = terminates the loop
#continue = skips to next iteration of the loop
#pass = does nothing, acts as a placeholder

#while True:
  #  name = input("What is your name?: ")
   # if name != "":
    #    break

phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")


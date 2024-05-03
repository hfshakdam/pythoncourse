#index operator [] = gives acess to a sequence's element
#e.g. (strings, lists, tuples)

name = "Hisham Shakdam"
#if(name[0].isupper()):#will determine true/false for capitalisation
 #   name = name.lower() #converts to lower case

first_name = name[0:6].upper()
last_name = name[7:].lower()
last_character = name[-1].upper() #negative indexing counts backwards

print(first_name)
print(last_name)
print(last_character)
#sets = an un-indexed and un-ordered collection with no dupe values

utensils = {"fork","knife","spoon"}
dishes = {"plates","cups","knife"}
#print(utensils) #when printing a set, it isn't always going to be in the same order
#makes it faster than lists to see if something is contained

#utensils.add("spork")
#utensils.remove("fork")
#utensils.update(dishes) #adds dishes to set of utensils

#print(utensils.difference(dishes))#prints what uten. has that dish. doesn't
#print(dishes.difference(utensils)) #same but flipped
print(utensils.intersection(dishes)) #shows what they have in common

#for x in utensils:
 #   print(x)
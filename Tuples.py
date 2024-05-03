#tuple = ordered collection and unchangeable
#used to group together related data

student = ("Hisham",22,"dropout")

print(student.count(22)) #count function returns no. of times an object appeared
print(student.index("Hisham")) #prints  the index value of "Hisham" in this case

for x in student:
    print(x)

if "Hisham" in student:
    print("Hisham is here!")
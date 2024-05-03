#slicing = creating a substring by extracting elements from another string
#indexing[] or slice()
#[start:stop:step]

#name = "Hisham Shakdam"
#first_name = name[0:6]
#computers start at value 0
#The 'start' is 'inclusive', meaning  the 0 includes the 'H' element
#The 'stop' is 'exclusive', meaning  the 5 doesn't include the 'm' element

#last_name = name[7:14]
#Short hand way to write it:

#first_name = name[:6] - python assumes blank - 0 because of the colon
#funky_name = name[0:14:2] #Will display every second character

#[0:14:4] would display every 4th character

#reversed_name = name[::-1]

#removing a colon takes away letters by the step value

#print(first_name, last_name)
#print("This is your funky name: ", funky_name)
#print(reversed_name)

website = "http://google.com"
website2 = "http://crunchy-roll.com"

slice = slice(7,-4) #acts like a modifier to variables
#the negative number represents a negative index counting backwards
#print(website[7:]) #leaving the step blank assumes the end of the string
print(website2[slice])

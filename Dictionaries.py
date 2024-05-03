#a changeable, unordered collection of unique {key:value} pairs
# fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington',
            'Germany':'Berlin',
            'Russia':'Moscow'}

capitals.update({'Russia':'St Petersburg'}) #modifies the dictionary
capitals.pop('Russia') #removes key:value pair
capitals.clear()#clears dictionary
#print(capitals['Germany'])
#print(capitals.get('China')) #checks to see if china is in your dictionary
#print(capitals.keys()) #prints only the keys (also work with values)
#print(capitals.items()) #prints entire dictionary

for key, value in capitals.items():
    print(key,value)
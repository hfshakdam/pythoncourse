#Used to check if one/two or more conditional statements are true (and, or, not)
#The 'not' operator flips things between false/ true
temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("What splendid weather!")
elif temp < 0 or temp > 30:
    print("bruh good-luck")
#elif temp > 30:
  #  print("Wear sunscreen today!")
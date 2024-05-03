#code that will only execute if condition is true

age = int(input("How old are you?: "))

if age == 100: #python thinks a single = is assigning a varible not checking for value, you have to use a double ==
    print("You are a century old, why are you still drinking..")
elif age >= 18:
    print("You are an adult! Here are your drinks..")
elif age < 0:
    print("You haven't been born yet and literally can't drink")
else:
    print("sorry kid, no drinks for you")
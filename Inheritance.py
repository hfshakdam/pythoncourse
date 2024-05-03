#inheritance allows classes to inherit the code of other classes
#You can have a parent and child class
class Animal:

    alive = True #this is a class variable

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):#the () makes Rabbit the child class to Animal
    def run(self):
        print("This rabbit is running")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

print(rabbit.alive)
fish.eat()
hawk.fly()
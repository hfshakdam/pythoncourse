class Car:
#might want to create objects on seperate modules if they are large, then just import them
    def __init__(self,make,model,year,colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    def drive(self): #"self" refers to the object
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+ " car is stopped")
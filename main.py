class Parrot:  
    species = "bird" 

    def __init__(self, name, age):   
        self.name = name   
        self.age = age  

    def display(self):    
        print(f"{self.species} name is {self.name}, it age is {self.age}")  

obj1 = Parrot("chiku", 1) 
obj1.display()   
obj2 = Parrot("magak", 4) 
obj2.display()
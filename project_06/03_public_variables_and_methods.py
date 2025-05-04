# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


class Car:
    
    def __init__(self, brand):
        self.brand = brand  
        
    def start(self):
        
        print(f"Start the engine of Babar Azam's Car {self.brand}")
        print(f"Vroom vroom! The {self.brand} roars to life!")
        


favCar = Car("Lamborghini Aventador")


favCar.start()



        
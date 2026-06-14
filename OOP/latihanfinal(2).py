class Vechile:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
        
    def move(self):
        print('Vechile is moving')
        
class Car(Vechile):
    def __init__(self,brand,speed):
        super().__init__(brand,speed)
        
    def move(self):
        print('Car is driving')

class Motorcycle(Vechile):
    def __init__(self,brand,speed):
        super().__init__(brand,speed)
        
    def move(self):
        print('Motorcycle is riding')


        
jalan = [
    Car('toyota',234),
    Motorcycle('Ducati',328)

]

for i in jalan:
    i.move()
    
    
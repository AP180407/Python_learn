# 1. Basic Class and Object
#    Problem: Create a Car class with attributes like brand and model. 
#             Then create an instance of this class.
class car:
    total_car = 0 # class variable
    def __init__(self, brand , model):
        self.__brand = brand # private variable
        self.model = model
        car.total_car += 1
    # 2. Class Method and Self
    # Problem: Add a method to the Car class 
    #          that displays the full name of the car (brand and model).
    # formated string for marg 2 or more functions
    def fullname(self):
        return f"{self.__brand} {self.model}" 
    
    @staticmethod
    def get_brand():
        return "car brand is TATA"
    
    def fule_type(self):
        return "pretrol and disel"
    


# 3. Inheritance
#    Problem: Create a subclass called ElectricCar that inherits from the Car class.
class electric_car(car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fule_type(self):
        return "electricity"
         

new_car = electric_car("Tesla", " Model L", "100kwh")
print(new_car.fullname())
print(new_car.battery_size)
print(new_car.get_brand())
print(new_car.fule_type())

my_car = car("TATA", "Grand i10 sportz") 
print(my_car.get_brand())
print(my_car.model) 
print(my_car.fullname())
print(my_car.fule_type())  

print(car.total_car)

class Battery:
    def battery_info(self):
        return "battery size is 100kwh"

class engine:
    def engine_info(self):
       return "engine type is V6"

class Elecric_car(Battery, engine , car):
    pass
   
Grand_vitara = Elecric_car("TATA", "Grand vitara")
# print(Grand_vitara.modele())
print(Grand_vitara.battery_info())     
print(Grand_vitara.engine_info())
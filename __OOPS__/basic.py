class Car:
    # count no of Car object created
    car_count = 0

    # method created
    def __init__(self,brand, model):
        # __brand makes it private
        self.__brand = brand
        self.__model = model
        Car.car_count += 1

    # getters
    def get_brand(self):
        return self.__brand
    

    def full_Name(self):
        # f" " is formatted string
        return f"{self.__brand} {self.__model}"
    
    # Polymorphism
    def fuel_type(self):
        return "Petrol or Diesel"
    
    # Static method accessible by only parent class not any object
    @staticmethod
    def general_description():
        return "car is means of transport"
    
    # used to hide property so that it cannot be overridden
    @property
    def model(self):
        return self.__model

# Inheritance
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        # To access any method from parent class we use super
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"
 
# __init__ is constructor of python
# self is just like this keyword in JAVA
# my car is a object of Car class


my_Car = Car("Toyota","Corolla")
# print(my_Car.brand)
# print(my_Car.model)
# print(my_Car.full_Name())


my_electric = ElectricCar("Tesla","Model 3","70kWH")
# print(my_electric.model)
# # print(my_electric.brand)
# print(my_electric.battery_size)
# print(my_electric.full_Name())
# print(my_electric.get_brand())
# print(my_electric.fuel_type())

Safari = Car("Tata","Safari")
# print(Safari.fuel_type())

Scorpio = Car("Tata","Scorpio")
# print(Car.car_count)

# print(Safari.general_description())
# print(Car.general_description())

# Safari.model = "City"
print(Safari.model)


# Checks whether given object is instance of given Class
# print(isinstance(my_electric,Car))
# print(isinstance(my_electric,ElectricCar))


# Multiple Inhertiance
class Battery():
    def battery_info(self):
        return "Battery is there"
    
class Engine():
    def engine_spec(self):
        return "No engine"

class ElectricTwo(Battery,Engine,Car):
    pass
    # def __init__(self, brand, model):
    #     super().__init__(brand, model)

my_tesla = ElectricTwo("Nicola","Badger")
print(my_tesla.full_Name())
print(my_tesla.model)
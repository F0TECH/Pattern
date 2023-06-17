from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class Ford(Car):
    def drive(self):
        print("Driving a Ford")

class Toyota(Car):
    def drive(self):
        print("Driving a Toyota")

class CarFactory:
    def create_car(self, car_type: str) -> Car:
        if car_type == "Ford":
            return Ford()
        elif car_type == "Toyota":
            return Toyota()
        else:
            raise ValueError("Invalid car type")

factory = CarFactory()
car = factory.create_car("Ford")
car.drive() # Driving a Ford
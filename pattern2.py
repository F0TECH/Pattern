class Car:
    def __init__(self):
        self.color = None
        self.engine = None
        self.tires = None

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_color(self, color):
        self.car.color = color
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_tires(self, tires):
        self.car.tires = tires
        return self

    def build(self):
        return self.car

builder = CarBuilder().set_color("red").set_engine("V6").set_tires(4)
car = builder.build()

print(car.color)
print(car.engine) # V6
print(car.tires) # 4
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def get_model(self):
        pass

class Sedan(Car):
    def get_model(self):
        return "Sedan"

class Coupe(Car):
    def get_model(self):
        return "Coupe"

class SUV(Car):
    def get_model(self):
        return "SUV"

class CarFactory(ABC):
    @abstractmethod
    def create_sedan(self) -> Sedan:
        pass

    @abstractmethod
    def create_coupe(self) -> Coupe:
        pass

    @abstractmethod
    def create_suv(self) -> SUV:
        pass

class FordFactory(CarFactory):
    def create_sedan(self) -> Sedan:
        return Sedan()

    def create_coupe(self) -> Coupe:
        return Coupe()

    def create_suv(self) -> SUV:
        return SUV()

class ToyotaFactory(CarFactory):
    def create_sedan(self) -> Sedan:
        return Sedan()

    def create_coupe(self) -> Coupe:
        return Coupe()

    def create_suv(self) -> SUV:
        return SUV()

class CarShop:
    def __init__(self, factory: CarFactory):
        self.factory = factory

    def get_coupe(self) -> Coupe:
        return self.factory.create_coupe()

    def get_sedan(self) -> Sedan:
        return self.factory.create_sedan()

    def get_suv(self) -> SUV:
        return self.factory.create_suv()

ford_factory = FordFactory()
toyota_factory = ToyotaFactory()

ford_shop = CarShop(ford_factory)
sedan = ford_shop.get_sedan()
print(sedan.get_model()) # Sedan

toyota_shop = CarShop(toyota_factory)
suv = toyota_shop.get_suv()
print(suv.get_model()) # SUV
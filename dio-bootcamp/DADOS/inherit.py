class Vehicle:
    def __init__(self, color, license_plate, number_wheel):
        self.color = color
        self.license_plate = license_plate
        self.number_wheel = number_wheel

    def turn_on(self):
         print(f"turn on {self.__class__.__name__}")

    def __str__(self):
        return f"{self.__class__.__name__} {', '.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}\n"


class Motorcycle(Vehicle):
    pass

class Car(Vehicle):
    pass

class Truck(Vehicle):
    def __init__(self, color, license_plate, number_wheel, loaded):
        super().__init__(color, license_plate,number_wheel)
        self.loaded = loaded

    def is_loaded(self):
        print(f"{'sim' if self.loaded else 'não'}")

moto = Motorcycle('black','abc_456',2)
moto.turn_on()
print(moto)

car = Car('black','asc_456',4)
car.turn_on()
print(car)

truck = Truck('black','asc-456', 4, False)
truck.turn_on()
truck.is_loaded()
print(truck)
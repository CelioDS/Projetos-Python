class SaveCar:
    def __init__(self):
        self.listCar = []



    def append_car(self,make, model, year, license_place):
        self.listCar.append([make, model, year, license_place])

    def show_car(self):

        for car in self.listCar:
            print(car)

addCar = SaveCar()


addCar.append_car('jaguar','jaguar 3', '2022','ds5sa6')
addCar.append_car(make='tesla', model='tesla 3', year='2022', license_place='ds5sa6')
addCar.append_car(**{'make':'ford','model':'mustang 3', 'year':'2022', 'license_place':'ds5sa6'})

addCar.show_car()


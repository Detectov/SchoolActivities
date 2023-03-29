class Car:
    def __init__(self, cp = "", m = "", b = "", y = 0, p = 0.0):
        self.__car_plate = cp
        self.__model = m
        self.__brand = b
        self.__year = y
        self.__price = p
    def printCarData(self):
        print(f"{self.__car_plate} {self.__model} {self.__brand} {self.__year}")
        print(f"Price: ${self.__price}")

class Company:
    def __init__(self, cn =""):
        self.name = cn
        self.car_list = []
    def add_car(self, car):
        self.car_list.append(car)
    def show_car_list(self):
        for car in self.car_list:
            car.printCarData()
            print()
    def show_carData(self, car_plate):
        for car in self.car_list:
            if car_plate == car.__car_plate:
                car.printCarData()
                break
            else:
                print("Car not found")
    def delete_car(self, car_plate):
        for index in range(0, len(self.car_list), 1):
            if self.car_list[index].__car_plate == car_plate:
                self.car_list.pop(index)
                break
            else:
                print("Car not found")
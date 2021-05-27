class Car:


    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"Создана машина: {self.name}, Цвет {self.color}, машина полицейская - {self.is_police}")

    def go(self):
        print(f"{self.name}: Машина поехала")

    def stop(self):
        print(f"{self.name}: Машина остановилась")

    def turn(self, direction):
        print(f"{self.name}: Машина повернула {'налево' if direction == 0 else 'направо'}")

    def show_speed(self):
        print(f"{self.name}: Скорость автомобиля - {self.speed}")

class WorkCar(Car):

    def show_speed(self):
        print(f"{self.name}: Скорость автомобиля - {self.speed} - ПРЕВЫШЕНИЕ СКОРОСТИ!!!" \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля - {self.speed}")


class TownCar(Car):

    def show_speed(self):
        print(f"{self.name}: Скорость автомобиля - {self.speed} - ПРЕВЫШЕНИЕ СКОРОСТИ!!!" \
            if self.speed > 60 else f"{self.name}: Скорость автомобиля - {self.speed}")


class SportCar(Car):
    """спооорт"""

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar('ДПС', 'Белый', 80)
police_car.go()
police_car.turn(0)
police_car.show_speed()

town_car = TownCar('Toyota', "синий", 50)
town_car.show_speed()
work_car =WorkCar('Камаз', "черный", 50)
work_car.go()
work_car.show_speed()


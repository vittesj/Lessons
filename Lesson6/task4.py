class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
        self.name = 'Car'
        self.is_police = False
        print(self.name, 'Полицейская?', self.is_police)

    def go(self):
        print(self.name, 'поехала')

    def stop(self):
        print(self.name, 'остановилась')

    def turn(self, direction):
        print(self.name, 'повернула', direction)

    def show_speed(self):
        print(self.name, 'имеет скорость', self.speed)


class TownCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color)
        self.name = 'town car'


class SportCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color)
        self.name = 'sport car'


class WorkCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color)
        self.name = 'work car'


class PoliceCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color)
        self.name = 'policy car'
        self.is_police = True


towncar=TownCar(60, 'black')
towncar.go()
towncar.show_speed()
towncar.turn()
towncar.stop()

sportcar = SportCar(60, 'black')
sportcar.go()
sportcar.show_speed()
sportcar.turn()
sportcar.stop()

workcar = WorkCar(60, 'black')
workcar.go()
workcar.show_speed()
workcar.turn()
workcar.stop()

policecar = PoliceCar(60, 'black')
policecar.go()
policecar.show_speed()
policecar.turn()
policecar.stop()
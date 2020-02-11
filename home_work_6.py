# Задание 1
import time


class TrafficLight:
    def __init__(self):
        self.__color = "red"

    def running(self):
        print("Запуск светофора...\n")
        if self.__color != "red":
            print("Поломка, запуск не удался")
            return
        print("Загорается:", self.__color)
        time.sleep(7)
        self.__color = "yellow"
        print("Загорается: ", self.__color)
        time.sleep(2)
        self.__color = "green"
        print("Загорается: ", self.__color)
        time.sleep(7)


a = TrafficLight()
a.running()
a.running()


# Задание 2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_calculation(self):
        return self._width * self._length * 25 * 5


r = Road(5000, 20)
print("Требуется асфальта", r.asphalt_calculation())


# Задание 3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.w_name = name
        self.w_surname = surname
        self.w_position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus


class Position(Worker):
    def get_full_name(self):
        return self.w_name + " " + self.w_surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


workk = Position("Иван", "Иванов", "Директор", 25000, 15000)
print("Сотрудник: {}, доход: {} рублей".format(workk.get_full_name(), workk.get_total_income()))


# Задание 4
class Car:
    def __init__(self, n, c, s, i):
        self.speed = s
        self.color = c
        self.name = n
        self.in_police = i

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина останавливается")

    def turn(self, derection):
        print("Машина поворачивает на ", derection)

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!")
        return Car.show_speed(self)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!")
        return Car.show_speed(self)


class PoliceCar(Car):
    pass


car1 = TownCar(input("Enter name town car: "), input("Enter color town car: "), 0.0, False)
car1.go()
car1.speed = float(input("Speed: "))
car1.turn("to the right")
print("Speed: ", car1.show_speed())
car1.stop()


# Задание 5
class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("отрисовка")


class Pen(Stationery):
    def draw(self):
        print("Отрисовка ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Отрисовка карандашем")


class Handle(Stationery):
    def draw(self):
        print("Отрисовка маркером")


a = Pen("ручка")
a.draw()
b = Pencil("ручка")
b.draw()
c = Handle("маркер")
c.draw()

# Домашнее задание по теме "Множественное наследование"
import random

class Animal:
    live = True
    sound = None            # звук(изначально отсутствует)
    _DEGREE_OF_DANGER = 0   # степень опасности существа
    # _cords = [0, 0, 0]      # координаты в пространстве

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # координаты в пространстве
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz  * self.speed < 0:
            print(f"It's too deep, i can't dive :(")
        else:
            self._cords = [dx * self.speed, dy * self.speed, dz * self.speed]

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(f'{self.sound}')


class Bird(Animal):
    beak = True # наличие клюва

    def lay_eggs(self):
        random.randint(1, 4)
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] = int(self._cords[2] - abs(dz) * self.speed / 2)
        self._cords[2] = max(self._cords[2], 0)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
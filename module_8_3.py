# Домашнее задание по теме "Создание исключений"


class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model          # название автомобиля (строка)
        self.__vin = __vin          # vin номер автомобиля (целое число)
        self.__numbers = __numbers  # номера автомобиля (строка)
        self.__is_valid_numbers()
        self.__is_valid_vin()

    def __is_valid_vin(self):
        if not isinstance(self.__vin, int):
            raise IncorrectVinNumber (f'Некорректный тип vin номер {self.model}')
        num = self.__vin
        if not 1000000 <= self.__vin <= 9999999:
            raise IncorrectVinNumber(f'Неверный диапазон для vin номера {self.model}')
        return True


    def __is_valid_numbers(self):
        if not isinstance(self.__numbers, str):
            raise IncorrectCarNumbers(f'Некорректный тип данных для номеров {self.model}')
        if not len(self.__numbers) == 6:
            raise IncorrectCarNumbers(f'Неверная длина номера {self.model}')


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
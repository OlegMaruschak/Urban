# Домашняя работа по уроку "Модули и пакеты"
from calendar import firstweekday


def divide(first, second):
    try:
        result = first / second
    except ZeroDivisionError:
        result = 'Ошибка.'
    return result

def main():
    first = int(input('Ведите делимое: '))
    second = int(input('Введите делитель: '))
    print(f'Результат деления {first} на {second} равен {divide(first, second)}')

if __name__ == '__main__':
    main()
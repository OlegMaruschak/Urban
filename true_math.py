# Домашняя работа по уроку "Модули и пакеты"

from math import inf

def divide(first, second):
    if second:
        result = first / second
    else:
        result = inf
    return result

def main():
    print(divide(5,0))

if __name__ == '__main__':
    main()
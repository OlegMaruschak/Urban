# Домашняя работа по уроку "Пространство имен."

def test_function():

    def inner_function():
        print('Я в области видимости функции test_function')

    print(inner_function())

print(test_function())
# print(inner_function()) # Ошибка: Имя 'inner_function' не определено. Вы имели в виду: 'test_function'?
# функция inner_function находится в локальном пространстве функции test_function
# не доступна в других пространствах проекта. Это и вызывает ошибку исполнения кода.
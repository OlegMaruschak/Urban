# Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции"

def personal_sum(numbers):
    rezult = 0
    incorrect_data = 0
    if isinstance(numbers, (str, list, type)):
        for num in numbers:
            try:
                rezult = rezult + num
            except TypeError:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {num}')
        return (rezult, incorrect_data)
    else:
        print('В numbers записан некорректный тип данных')

def calculate_average(numbers):
    try:
        rezult = personal_sum(numbers)
        if rezult != None:
            rezult_sum = rezult[0]
            average = rezult_sum / len(numbers)
            return average
    except ZeroDivisionError:
        return 0


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
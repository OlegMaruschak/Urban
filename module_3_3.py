# Самостоятельная работа по уроку "Распаковка позиционных параметров"

# 1. Функция с параметрами по умолчанию:
print('1. Функция с параметрами по умолчанию:')
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = 0, b = 'один', c = [2, 3, 4, 5])
print_params(a = 'zero', b = 'one')
print_params(b = 25)
print_params(c = [1, 2, 3])
print('\n')

# 2. Распаковка параметров:
print('2. Распаковка параметров:')
values_list = [2024, 'октябрь', True]
values_dict = {'a': 12, 'b': 'октября', 'c': False}
print_params(*values_list)
print_params(**values_dict)
print('\n')

# 3. Распаковка + отдельные параметры:
print('3. Распаковка + отдельные параметры:')
values_list_2 = ['apple', False]
print_params(*values_list_2, 42)
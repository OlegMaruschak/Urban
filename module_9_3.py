# Домашнее задание по теме "Генераторные сборки"


first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Первый вариант
zp = zip(first, second)
first_result = (len(a[0]) - len(a[1]) for a in zp if len(a[0]) != len(a[1]))
print(list(first_result))

# Второй вариант
first_result = (len(a) - len(b) for a, b in zip(first, second) if len(a) != len(b))
print(list(first_result))

second_result = (len(first[a]) == len(second[a]) for a in range(len(first)))
print(list(second_result))
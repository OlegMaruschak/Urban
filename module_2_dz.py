# Дополнительное практическое задание по модулю*
# Модуль 2. Основные операторы

number = int(input('Введите число от 3 до 20: '))
if 3 <= number <= 20:
    list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    password_ = ''

    for i in range(len(list_)):
        if number / 2 > list_[i]:
         for j in range(i + 1, len(list_)):
                if not (number % (list_[i] + list_[j])):
                 password_ = password_ + str(list_[i]) + str(list_[j])
    print('Ваш пароль: ' + password_)
else:
    print('Введенное число не корректно, перезапустите код и укажите число из предлагаемого диапазона.')
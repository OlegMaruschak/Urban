# Домашнее задание по теме "Введение в функциональное программирование"


def apply_all_func(int_list, *functions):
    result = {}
    for int_l in int_list:
        if isinstance(int_l,(int, float)):
            pass
        else:
            return 'Не корректный список, содержит не числовой элемент.'

    for func in functions:
        # print(func(int_list))
        result[func.__name__] = func(int_list)

    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
# Самостоятельная работа по уроку "Рекурсия"

def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        result_proc = first * get_multiplied_digits(int(str_number[1:]))
    else:
        result_proc = int(str_number[0])
    return result_proc

result = get_multiplied_digits(40203)
print(result)

result = get_multiplied_digits(12345)
print(result)
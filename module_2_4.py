# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(1, len(numbers)):
    is_prime = True
    for j in range(1, len(numbers)):
        #n1 = numbers[i] # диагностическая переменная
        #n2 = numbers[j] # диагностическая переменная
        if numbers[i] == numbers[j]:
            is_prime = True
            break
        elif numbers[i] % numbers[j] != 0:
            is_prime = True
        elif numbers[i] % numbers[j] == 0:
            is_prime = False
            break
    if is_prime == True:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print(primes)
print(not_primes)
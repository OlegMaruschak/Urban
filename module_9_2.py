# Домашнее задание по теме "Списковые, словарные сборки"


first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(a) for a in first_strings if len(a) > 5]
print(first_result)
second_result = [(a, b) for a in first_strings for b in second_strings if len(a) == len(b)]
print(second_result)
third_result = [{a : len(a)} for a in first_strings + second_strings if len(a) % 2 == 0]
print(third_result)
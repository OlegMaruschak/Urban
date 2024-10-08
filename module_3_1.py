# Домашняя работа по уроку "Пространство имён"

def count_calls():
    global calls
    calls += 1
    #return calls

def string_info (string_):
    count_calls()
    tuple_ = len(string_), string_.upper(), string_.lower()
    return tuple_

def is_contains (string_, list_):
    count_calls()
    for i in range(len(list_)):
        if string_.lower() in list_[i].lower():
            aaa = True
            return aaa
            break
    aaa = False
    return aaa


calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('Urban', ['urBAN', 'BaNaN', 'ban'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

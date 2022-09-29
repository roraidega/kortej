dictionary = {
    1: 'Лера',
    2: 'Аня',
    3: 'Виталик',
    4: 'Алекс',
    5: 'Софа'
}
addr = id(dictionary)

dictionary[1], dictionary[5] = dictionary[5], dictionary[1]
dictionary.pop(2)
dictionary['new_key'] = 'new_value'
print(dictionary)

print(id(dictionary) == addr)
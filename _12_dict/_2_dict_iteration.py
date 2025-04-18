person = {
    'name': 'Bob',
    'age': 30,
    'city': 'Moscow'
}

# Вывод пар (ключ, значение)
for item in person.items():
    print(item)        # Кортеж ('ключ', значение)
    print(type(item))  # <class 'tuple'>

# Распаковка ключа и значения
for key, value in person.items():
    print(key, value)

# Только ключи
for key in person.keys():
    print(key)

# Только значения
for value in person.values():
    print(value)

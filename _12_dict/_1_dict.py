# Простейший словарь
person = {
    'name': 'Bob',
    'age': 30
}

# Можно создать другой словарь по аналогии
person2 = {'name': 'Alice', 'age': 20}

# Добавление нового ключа
person['city'] = 'Moscow'

# Изменение значения по ключу
person['name'] = 'Ivan'

print(person)  # {'name': 'Ivan', 'age': 30, 'city': 'Moscow'}

# Получение значений
print(person.get('name'))  # 'Ivan'
print(person.get('job'))   # None (ключа нет, ошибки не будет!)


# Порядок ключей не важен
person = {
    'name': 'Bob',
    'age': 30
}

other_person = {
    'age': 30,
    'name': 'Bob'
}

print(person == other_person)  # True



# Объединение двух словарей
person_info = {
    'job': 'developer',
    'city': 'Moscow'
}

# Обновляем первый словарь значениями второго
person.update(person_info)
print(person)

# Альтернатива: объединение с оператором | (Python 3.9+)
person = person | person_info
print(person)

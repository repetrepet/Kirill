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

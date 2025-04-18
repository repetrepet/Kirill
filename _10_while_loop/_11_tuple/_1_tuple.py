# Кортеж — это как список, но его элементы нельзя изменять
user_roles = ('admin', 'editor', 'viewer')

# user_roles.append('bob')  # Ошибка! У кортежей нет метода append

print(len(user_roles))  # Длина кортежа: 3

# Перебор кортежа
for i in user_roles:
    print(i)

# Проверка вхождения элемента
print('admin' in user_roles)  # True
print('bob' in user_roles)    # False

# Обращение по индексу
print(user_roles[2])  # 'viewer'

# Распаковка значений
u1, u2, u3 = user_roles
print(u1, u3)  # 'admin viewer'

# Кортеж с одним элементом — обязательно с запятой!
user = ('admin',)
print(user)
print(type(user))  # <class 'tuple'>

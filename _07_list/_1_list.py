# 📌 Работа со списками (list) в Python

# Создание списков
fruits = ['apple', 'banana', 'cherry']  # Создание списка с элементами
print(fruits)

my_list = list()  # Создание пустого списка
print(my_list)

# Длина списка
print(len(fruits))

# Список с разными типами данных
my_list = [1, 'apple', True, 1.5, [1, 2, 3]]
print(my_list)

# Сравнение списков
list_1 = [1, 2, 3]
list_2 = [1, 3, 2]
list_3 = [1, 2, 3]
print(list_1 == list_2)  # False
print(list_1 == list_3)  # True

# Проверка списка на пустоту
print(bool([]))  # False
print(bool([0]))  # True

# Проверка наличия элемента в списке
print('apple' in fruits)  # True
print('melon' in fruits)  # False

# Создание списка из переменных
element_1 = 'apple'
element_2 = 'banana'
element_3 = 'cherry'
my_list = [element_1, element_2, element_3]
print(my_list)

# Преобразование строки в список
word = 'Hello'
my_list = list(word)
print(my_list)

# Объединение списков
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = list_2 + list_1
print(list_3)

# 📌 Методы списков

# Добавление элемента в конец списка
fruits.append('melon')
print(fruits)

# Удаление элемента по индексу
fruits.pop(1)  # Удаление элемента с индексом 1 (banana)
print(fruits)

# Объединение списков
fruits1 = ['apple', 'banana', 'cherry']
fruits2 = ['orange', 'grape']
fruits1.extend(fruits2)
print(fruits1)

# Сортировка списка
my_list = [5, 4, 8, 10, 1, 2, 14, 4]
my_list.sort()
print(my_list)  # Сортировка по возрастанию
my_list.sort(reverse=True)
print(my_list)  # Сортировка по убыванию

# Разбиение строки в список
my_string = 'My name is Bob'
my_list = my_string.split()
print(my_list)

# Объединение списка в строку
l = ['My', 'name', 'is', 'Bob']
joined_string = '!'.join(l)
print(joined_string)

# Функции для работы со списками
print(sum(my_list))  # Сумма элементов списка
print(max(my_list))  # Максимальный элемент
print(min(my_list))  # Минимальный элемент
print(len(my_list))  # Длина списка

# Добавление элемента при условии
l = [1, 3, 6]
if len(l) > 5:
    l.append(10)
print(l)

# Запрос строки у пользователя и разбиение на слова
my_string = input("Введите строку:")
my_list = my_string.split()
print(my_list)

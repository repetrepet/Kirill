# 📌 Индексы в списках и строках
fruits = ['apple', 'banana', 'cherry']
string = 'Hello, world!'
print(string[0])  # Первый символ
print(string[-1])  # Последний символ
print(fruits[0])  # Первый элемент списка
print(fruits[-1])  # Последний элемент списка

# Изменение элемента списка
fruits[1] = 'ORANGE'
print(fruits)

# 📌 Работа с числами

# Получение первой цифры числа
number = input("Введите число:")
print(number[0])

# Получение последней цифры числа
my_number = 456 
print(str(my_number)[-1])

# Сумма первой и последней цифры числа
my_number = 698876587587876570
first_digit = str(my_number)[0]
last_digit = str(my_number)[-1]
print(int(first_digit) + int(last_digit))

# Количество цифр в числе
my_number = int(input("Введите число: "))
print(len(str(my_number)))

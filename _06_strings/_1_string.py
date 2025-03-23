# Строки (String)

# Объявление строковых переменных
my_string1 = 'Hello, world!'
my_string2 = "Hello, world!"

# Вывод строк в консоль
print(my_string1)
print(my_string2)

# Многострочная строка
my_string = """Hello, friend!
Hello from Russia!
"""
print(my_string)

# Объединение строк (конкатенация)
first_name = 'Bob'
last_name = 'Brown'
full_name = first_name + ' ' + last_name  # Объединение строк с пробелом
print(full_name)

# Длина строки
print(len(full_name)) 

# Приведение к строковому типу данных
my_integer = 100
my_string = str(my_integer)  # Преобразование числа в строку
print(type(my_integer))
print(type(my_string))

age = 30
print('Человеку ' + str(age) + ' лет')  # Конкатенация с приведением числа к строке

# Приведение из строки в число
string = '45'
print(int(string) / 9)  # Преобразование строки в число и деление

x = input('Введите число: ')
print(type(x))  # Тип данных введенной строки
integer = int(x)  # Преобразование строки в число
print(type(integer))

# Длина числа, представленного строкой
big_integer = 2 ** 1000
length = len(str(big_integer))
print(length)

# Проверка наличия символов в строке
string = 'Hello, world!'
print('o' in string)
print('x' in string)
print('Hello' in string)
print('hello' in string)  # Учитывается регистр букв

# Строковые методы

# Превратить все буквы в заглавные/строчные
my_string = 'Kirill'
print(my_string.upper())  # Все буквы заглавные

my_string = 'KIRILL'
print(my_string.lower())  # Все буквы строчные

# Обрезает лишние пробелы по бокам
my_string = '   Hello!       '
print(len(my_string))  # Длина строки с пробелами
print(my_string.strip())  # Удаление пробелов по бокам
print(len(my_string.strip()))  # Длина строки после удаления пробелов

# Замена подстроки в строке
my_string = 'Hello, world!'
print(my_string)
print(my_string.replace('world', 'Python'))  # Заменяем 'world' на 'Python'

# Подсчет количества вхождений подстроки
my_string = 'Hello, world!'
print(my_string.count('world'))
print(my_string.count('l'))

# Проверка, состоит ли строка только из цифр
my_string = '10'
print(my_string.isdigit())  # Вернет True

my_string = '10h'
print(my_string.isdigit())  # Вернет False

# Форматирование строк
age = 30
print(f'Человеку {age} лет')  # Использование f-строк

x = 5
y = 10
print(f'Сумма чисел: {x + y}\nПроизведение чисел: {x * y}')

# Удаление всех пробелов из введенной строки
my_string = input("Введите строку: ")
print(my_string.replace(" ", ""))

# Замена всех вхождений одного символа в строке
my_string = input("Введите строку: ")
old_symbol = input("Введите старый символ: ")
new_symbol = input("Введите новый символ: ")
print(my_string.replace(old_symbol, new_symbol))

# Подсчет количества слов в строке
my_string = input("Введите строку: ")
print(len(my_string.split()))  # Разбивает строку по пробелам и считает слова

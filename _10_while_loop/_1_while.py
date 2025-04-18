# Простой цикл while
x = 1

# Цикл выполняется, пока x меньше 5
while x < 5:
    print(f'X равен: {x}')
    x += 1  # Увеличиваем значение x на 1

print('Конец цикла!')


# Цикл while с условием на непустой список
my_list = [0, 1, 2]

# Пока список не пустой, будет выполняться цикл
while my_list:
    element = my_list.pop()  # Удаляем последний элемент из списка и сохраняем в переменную
    print(f'Element равен {element}')  # Выводим удалённый элемент

print(my_list)  # Пустой список


# Пример бесконечного цикла
# Внимание: остановить можно вручную (Ctrl+C)
# while True:
#     print('Это бесконечный цикл!')


# Цикл while с условием выхода
# Пользователь вводит данные, пока не введёт 'quit'

while True:
    answer = input('Введите число: ')
    if answer == 'quit':
        break  # Прерываем цикл
    print(f'Вы ввели: {answer}')


# Задача: суммировать числа, вводимые пользователем, пока не введено 'quit'
summa = 0  # Переменная для хранения суммы

while True:
    answer = input("Введите число: ")
    if answer == "quit":
        break  # Завершаем цикл
    summa += int(answer)  # Преобразуем ввод в число и добавляем к сумме

print(f"Сумма равна {summa}")

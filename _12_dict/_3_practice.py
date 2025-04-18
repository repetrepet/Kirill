# Собрать дату из словаря
data = {
    'year': '2025',
    'month': '12',
    'day': '31',
}

# Сборка строки с датой в нужном формате
print(f"{data['year']}-{data['month']}-{data['day']}")  # '2025-12-31'


# Задача: найти сумму квадратов значений в словаре
data = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

summa = 0
for value in data.values():
    value = value**2  # Возводим значение в квадрат
    summa += value    # Прибавляем к общей сумме

print(summa)  # 1 + 4 + 9 + 16 = 30

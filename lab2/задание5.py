# Создаем список чисел от 1 до 20
numbers = list(range(1, 21))

# Фильтруем четные числа с помощью filter() и лямбда-функции:
# filter(lambda x: x % 2 == 0, ...) → оставляет только элементы, для которых лямбда возвращает True
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # Лямбда проверяет четность x

# Увеличиваем каждое число на 10 с помощью map() и лямбда-функции:
# map(lambda x: x + 10, ...) → применяет лямбду ко всем элементам списка
incremented = list(map(lambda x: x + 10, even_numbers))  # Лямбда добавляет 10 к x

# Сортируем список по убыванию (лямбда не используется, но reverse=True меняет порядок)
sorted_numbers = sorted(incremented, reverse=True)

# Выводим результаты
print("Исходный список:", numbers)
print("Четные числа:", even_numbers)
print("Увеличенные на 10:", incremented)
print("Отсортированные по убыванию:", sorted_numbers)
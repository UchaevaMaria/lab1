import random
rannum = [random.randint(1,100)for _ in range(10)]#генератор списка от 1 до 100
print("Исходный список:", rannum)
#нахождение минимального и максимального значения
maxim = max(rannum)
mini = min(rannum)
print("Максимальное значение:",maxim, "Минимальное значение",mini)
#сумма всех элементов 
summ = sum(rannum)
print("Сумма всех элементов:", summ)
rannum.sort()
print("Отсортированный список:", rannum)
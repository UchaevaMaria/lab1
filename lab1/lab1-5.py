import random
random_numbers = [random.randint(1, 100) for _ in range(20)]
even_numbers = [] #создаем пустой список
for number in random_numbers:  #перебор каждого значения
    if number % 2 == 0:  #если остаток 0
        even_numbers.append(number)  #добавляем значение в список 
print("четные:", even_numbers)
#на 3, менее громозд версия кода
divisible3 = [number for number in random_numbers if number % 3 == 0]
print("на 3",divisible3)
total = 0   #добавляем перемнную
for number in random_numbers:  #перебор
    total = total + number #добавляем в переменную значение
count = len(random_numbers) #кол-во эл в списке
average = total / count  #cреднее арфм

print("Среднее арифметическое:",average)
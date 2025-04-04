numbers = [] #создаем пустой список
with open("data.txt", "r", encoding="cp1251") as file: #вызываем встроенную функцию open(), указываем нужную кодировку, даем переменной название "file"
    for line in file:
        number = int(line.strip()) #перебора содержимого файла по одной строке 
        numbers.append(number) #добавляем каждый элемент в список
    print(numbers) #принтую для проверки
    total = sum(numbers) #нахожу сумму
    average = total / len(numbers) #нахожу ср.арифм
    maximum = max(numbers) #нахожу max
    minimum = min(numbers) #нахожу min
    #ввожу переменную и с помощью f строки вставляю вычисленные значения
    results = f"""Сумма: {total} 
Среднее: {average}
Максимум: {maximum}
Минимум: {minimum}"""
with open("result.txt", "w",encoding="utf-8") as outfile: #создаем и открываем файл «result.txt», кодировка UTF-8 для записи в файл  
            outfile.write(results) #записываем в файл содержимое переменной results
print("Результат находится result.txt")#принтую для удобства
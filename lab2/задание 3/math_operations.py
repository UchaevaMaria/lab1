# math_operations.py
def add(a, b):
 #Возвращает сумму двух чисел
    return a + b
def subtract(a, b):
 #Возвращает разность двух чисел.
    return a - b

def multiply(a, b):
#Возвращает произведение двух чисел."""
    return a * b

def divide(a, b):
#Возвращает результат деления a на b. Обрабатывает деление на ноль."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль невозможно."
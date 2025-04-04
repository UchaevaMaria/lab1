try:
    nm1 = int(input("Введите первое число"))
    nm2 = int(input("Введите второе число"))
    result = nm1/nm2
except ValueError:
    print("Ошибка: Введено нечисловое значение, попробуйте заново.")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль, попробуйте заново.")
else:
    print(f"Результат деления: {result}")
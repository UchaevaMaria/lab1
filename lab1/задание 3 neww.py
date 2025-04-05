n = int(input())
while n >= 1:          # Выводит все числа от n до 1
    for i in range(n): #перебор
        print((n-i))
    break
n1 = n #cохр первоначальное число n для факториала
m = 1        # Выводит факториал всех чисел от 1 до n
while n >= 0:
    if n != 0:
        for i in range(1, n + 1):
            m*= i
        print(m)
        break
    else:
        print(1)
        break

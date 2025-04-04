n = int(input())
n1 = n #cохр первоначальное число n для факториала
if n<=0:
    print("Введите целое положительное число")
else:
    while n!=0: #пока число н не равно нулю, мы выполняем:
        print(n % 10, end="") #печатаем последнее значение
        n = n//10 # отсекаем 
    print() #перенос
    factorial = 1 
    while n1> 1:
        factorial *= n1 
        n1-= 1

    print(factorial)
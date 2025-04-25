#угадайка(1)
import random
from datetime import datetime
def gener_num():  # возвращает рандомное число
    return random.randint(1, 100)
def get_pl_num():
    while True:  # цикл для повторного ввода при некорректном числе
        try:
            num = int(input("Введите число: "))
            if 1 <= num <= 100:
                return num
            else:
                print("Введите допустимое число от 1 до 100")
        except ValueError:
            print("Некорректный ввод. Введите целое число.")

def game_start1():  # начало нашей игры
    time_start = datetime.now()
    print(f"Давайте угадаем число, время начала игры: {time_start}")
    randnum = gener_num()
    print(randnum)
    attempts = 0  #  счетчик попыток
    go = get_pl_num()

    while go != randnum:
        attempts += 1  # увеличиваем счетчик попыток
        if go > randnum:
            print("Слишком много! время текущей попытки:", datetime.now())
        elif go < randnum: 
            print("БОЛЬШЕ! время текущей попытки:", datetime.now())
        go = get_pl_num()  # Запрашиваем новое число внутри цикла
    attempts += 1  # счетчик попыток после угадывания
    over_time = datetime.now() - time_start 
    m = save_result(attempts, over_time)
    print(f"Поздравляю! Это верно, вы угадали число {randnum} за {attempts} попыток и потратили: {over_time}")
    return attempts, str(over_time) # возвращаем результаты игры

def save_result(attempts, over_time_str): #сохранение игры в файл
    with open("game_res.txt", "w") as file:
        file.write(f"Дата: {datetime.now()}, Попытки: {attempts}, Время: {over_time_str}")
        print("Результаты игры сохранены в файл 'game_res.txt'")

if __name__ == "__main__":
    attempts, over_time_str = game_start1()
    save_result(attempts, over_time_str)
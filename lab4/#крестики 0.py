#крестики 0
print('Добро пожаловать')
board = list(range(1, 10))  #создаем список от 1 до 9
def draw_board(board):
    print("_" * 13)
    for i in range(3):
        print('|', board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("_" * 13)

def take_input(board, sim):  # Передаем board как аргумент
    flag = False
    while not flag:
        play_ans = input(f"Куда введем {sim}? ") 
        try:
            play_ans = int(play_ans)
        except ValueError:
            print("Введите корректное число")
            continue
        if 1 <= play_ans <= 9:
            if str(board[play_ans - 1]) not in 'X0':
                board[play_ans - 1] = sim
                flag = True
            else:
                print("Эта клетка занята")
        else:
            print('Введите допустимое число от 1 до 9')

def check_win(board):
    win_cod = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)) 
    for ind in win_cod:
        if board[ind[0]] == board[ind[1]] == board[ind[2]]:
            return board[ind[0]]  #возвращаем символ победителя
    return False

def main(board):  #передаем board как аргумент
    count = 0
    game_over = False 
    while not game_over:
        draw_board(board)
        if count % 2 == 0:
            take_input(board, 'X')  
        else:
            take_input(board, "0")  
        count += 1  
        winner = check_win(board)
        if winner:
            draw_board(board) #выводим финальное поле
            print(winner, "выиграл!")
            game_over = True
        elif count == 9:
            draw_board(board) #выводим финальное поле
            print("НИЧЬЯ!")
            game_over = True

#запускаем игру
main(board)
import random

def deal_card(): #возвращает рандом карту
    return random.randint(2, 11)

def calculate_score(cards): #подсчитывает сумму
    return sum(cards)

def play_game(): #запуск игр
    player_cards = []
    dealer_cards = []

    player_cards.append(deal_card())
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())

    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"Ваши карт:{player_cards}, Счет:{player_score}")
    print(f"Карты дилера: {dealer_cards[0]}, Y")
    while player_score <= 21:
        choose_action = input("Взять карту (1) или остановиться (2)? ").lower()
        if choose_action == '1':
            new_card = deal_card()
            player_cards.append(new_card)
            player_score = calculate_score(player_cards)
            print(f'Вы взяли карту: {new_card}, Ваши карты:{player_cards}, Нынешний счет:{player_score}')
            if player_score>21:
                print("Перебор! Вы проиграли.")
        else:
            print("Вы остановились.")
            break  # переход к ходу дилера
    print(f"Карты дилера: {dealer_cards}, Счет: {dealer_score}")  #  карты дилера
    while dealer_score < 17 and player_score <= 21:  # дилер берет карты, пока у него меньше 17
        new_card = deal_card()
        dealer_cards.append(new_card)
        dealer_score = calculate_score(dealer_cards)
        print(f"Дилер взял карту {new_card}. Карты дилера: {dealer_cards}, Счет: {dealer_score}")
    if player_score <= 21:  # проверяем, что не проиграл 
        if dealer_score > 21:
            print("У дилера перебор! Вы выиграли.") 
        elif player_score > dealer_score:
            print("Вы выиграли!")
        elif player_score < dealer_score:
            print("Вы проиграли.")
        else:
            print("Ничья!")
if __name__ == "__main__":
    play_game()


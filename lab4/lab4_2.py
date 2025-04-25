import random

def deal_card():
    """Возвращает случайную карту (значение от 2 до 11)."""
    return random.randint(2, 11)

def calculate_score(cards):
    """Подсчитывает сумму очков в руке."""
    return sum(cards)

def play_game():
    """Запускает игру '21'."""
    player_cards = []
    dealer_cards = []

    # 1. Начальная раздача карт
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
            break  # Переход к ходу дилера
    print(f"Карты дилера: {dealer_cards}, Счет: {dealer_score}")  # Раскрываем карты дилера
    while dealer_score < 17 and player_score <= 21:  # Дилер берет карты, пока у него < 17 и игрок не проиграл
        new_card = deal_card()
        dealer_cards.append(new_card)
        dealer_score = calculate_score(dealer_cards)
        print(f"Дилер взял карту {new_card}. Карты дилера: {dealer_cards}, Счет: {dealer_score}")
    if player_score <= 21:  # Проверяем, что игрок не проиграл
        if dealer_score > 21:
            print("У дилера перебор! Вы выиграли.")  # Это условие уже проверено в цикле выше, но оставим для ясности
        elif player_score > dealer_score:
            print("Вы выиграли!")
        elif player_score < dealer_score:
            print("Вы проиграли.")
        else:
            print("Ничья!")
if __name__ == "__main__":
    play_game()


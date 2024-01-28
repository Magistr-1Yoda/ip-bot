import random 

worlds = ["ковров", "владимир", "куб", "шаурма", ]


def get_ask():
    return random.choice(worlds)

def play(word):
    word_ask = "*" * len(word)
    hp = 10
    win = False
    print(f"Я загадал слово, его длина: {word_ask}")
    while not win and hp > 0:
        ask = input('Введите любую букву или целое слово: ').lower()
        if ask in word:
            print(f'Отличная работа, буква {ask} есть в слове')
            word_as_list = list(word_ask)
            indices = [i for i in range(len(word)) if word[i] == ask]
            for index in indices:
                word_as_list[index] = ask
                word_ask = ''.join(word_as_list)
                if '*' not in word_ask:
                    win = True
        else:
            hp -= 1
            print(f'Буквы нет в слове! Осталось {hp} попыток')
        print(f"Ваша слово: {word_ask}")
      
        if ask in worlds:
            print(f'Отлично вы угадали, целое слово: {ask}')
        else:
            hp -= 5
            print(f'Вы ошиблись, у вас осталось попыток {hp}')
again = '1'
while again == '1':
    word = get_ask()
    play(word)
    again = input('Играем ещё раз?\n1-да 2-нет \n')


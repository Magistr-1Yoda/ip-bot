from random import *
score_gamer = 0
score_computer = 0
def random_numbers():
    return randint(1, 6)
print('Привет, давай поиграем в кости')
while True:
    gamer = input('Бросишь кубики?\n1-Да✔️ \n2-Нет❌ \n')
    if gamer == "1":
        gamer_cube = random_numbers()
        computer_cube = random_numbers()
        if gamer_cube > computer_cube:
            print(f'Победа!🏆 Вам выпало {gamer_cube} а компьютеру {computer_cube}')
            score_gamer += 1
            print(f"Ваш счёт с компьютером {score_gamer}:{score_computer} ")
        elif computer_cube > gamer_cube:
            print(f'Поражения!❌Вам выпало {gamer_cube} а компьютеру {computer_cube}')
            score_computer +=1
            print(f"Ваш счёт с компьютером {score_gamer}:{score_computer}")
        elif gamer_cube == computer_cube:
            print("Ничья!😑")
    elif gamer == '2':
        print("До встречи, встретимся в следущий раз🤗")
        break
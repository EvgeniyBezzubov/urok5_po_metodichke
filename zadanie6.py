import random
def recurs(rand = random.randint(0, 100), trying=0):

    trying+=1
    try_p = int(input("введите загаданное число "))
    if try_p == rand:
        print("Вы угадали!")
    else:
        print("Вы НЕ угадали! Текущая попытка {0}, максимум 10".format(trying))
        if try_p < rand:
            print("Введённое число меньше")
        else:
            print("Введённое число больше")
        if trying<=10:
            recurs(rand, trying)
        else:
            print("Слишком много попыток, правильный ответ: ", rand)

recurs()

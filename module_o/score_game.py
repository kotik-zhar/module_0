import numpy as np
'''Алгоритм угадывает за 5 попыток'''


def game_core(number):
    '''Создаем переменную счетчик попыток, минимальное и максимальное возможное
    значение числа, вычесляем среднее арифметическое между минимальным
    и максимальным значение и проверяем его, меняем значение переменной
    максимальное и минимальноечисло в зависимости от ответа компьютера
    Функция принимает загаданное число и возвращает число попыток'''

    counter = 1                    # Счетчик попыток
    min_number = 1                 # Минимальное число
    max_number = 100               # Максимальное число
    predict = (max_number - min_number)//2
    while number != predict:
        counter += 1
        if number > predict:
            min_number = predict
            if max_number-min_number != 1:
                predict += (max_number-min_number)//2
            else:
                predict += 1
                break

        elif number < predict:
            max_number = predict
            if max_number-min_number != 1:
                predict -= (max_number-min_number)//2
            else:
                predict -= 1
                break

    return(counter)  # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать,
    как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, что воспроизводит эксперимент
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return(score)


score_game(game_core)

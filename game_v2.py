"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict():
    
    predict_number = np.random.randint(1, 101)
    findnumber = 50
    min_numb = 0
    max_numb = 100
    count = 1
    i = 0
    while findnumber != predict_number:
        if predict_number > findnumber:
            min_numb = findnumber
        else:
            max_numb = findnumber
        if i == 0:
            findnumber = (max_numb + min_numb) // 2 + 1
            i = 1
        else:
            findnumber = (max_numb + min_numb) // 2
            i = 0
        count += 1

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for i in random_array:
        count_ls.append(random_predict())

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)

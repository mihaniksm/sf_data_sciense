'''Игра угадай число
Компьютер сам загадывает и сам угадывает число'''

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count+=1
        predict_number = np.random.randint(1, 101) # предполагаемое число
    
        if predict_number == number:
            break # выход из цикла после угадывания
        
    return(count)

def score_count(random_predict) -> int:
    """Сколько в среднем угадывает  за 1000 попыток

    Args:
        random_predict ([type]): Функция угадывания

    Returns:
        int: Средее количество попыток
    """
    count_ls = []
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  #загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает в cреднем за {score} попыток')
    return(score)


if __name__ == '__main__':
    #RUN
    score_count(random_predict)

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
    left_borger = 0 # левая граница 
    right_border = 101 # правая граница
    predict_number = np.random.randint(1, 101) # число предполагаемое, компьютером 
    
    print(f'Загадано число:  {number}')
    print(f'Компьютер угадывает с:  {predict_number}')
   
    while True:
        count += 1
        print(f'Шаг №:  {count}')     
        
        if number == predict_number:
            print('Great')
            break
                
        elif number > predict_number:
            left_borger = predict_number
            print(f'Теперь левая граница:  {left_borger}')
            
        elif number < predict_number:
            right_border = predict_number 
            print(f'Теперь правая граница:  {right_border}')  
              
        predict_number = (left_borger + right_border)//2 
        
    return (count)
                
random_predict(50)

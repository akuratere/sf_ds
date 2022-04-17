''' Game 'guess the number' '''
'''Computer guesses the number'''

import numpy as np
def random_predict(number:int = 1) -> int:
    """randomly guessing the numbers

    Args:
        number (int, optional): number that is set. Defaults to 1.

    Returns:
        int: number of tries
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
        
    return count

def score_game(random_predict) -> int:
    """Calculating the average amount of tries

    Args:
        random_predict (_type_): function of guessing the number

    Returns:
        int: average number of guesses
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size = 1000) #list of 1000 numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Your algorithm guesses the number in average of {score} tries')
    return score
    
if __name__ == '__main__':
    score_game(random_predict)
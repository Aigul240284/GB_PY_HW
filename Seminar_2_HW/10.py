# Задача 10 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2
import random
import os
os.system('cls')
def mones(N):
    heads_tails=[]
    for _ in range(num_coins):
        heads_tails.append(random.randint(0, 1))
    print(heads_tails)
    tails=heads=0
    for item in heads_tails:
        if item == 0:
            tails+=1
        else: 
            heads+=1
    if tails < heads:
        return(f'You can flip {tails} coins')
    else: return(f'You can flip {heads} coins')
try:
    num_coins = int(input('TASK №10: Input the number of coins: '))    
    print(mones(num_coins))
except:
    print(f'Iinvailid input, please, try again.')


    

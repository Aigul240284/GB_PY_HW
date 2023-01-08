# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# Input: 4
# (значения сгенерированы случайным образом
# 4 2 3 1 )
# Output: 9
import math
import random
import os
os.system('cls')
bushes = int(input('Input number of bushes: '))
berry = list(random.randint(1, 5) for i in range(bushes))
print('berry harvest: ', berry)


def max_harvest1(list_1):
    list_2 = []
    for i in range(len(list_1)-1):
        list_2.append(list_1[i-1]+list_1[i]+list_1[i+1])
    list_2.append(list_1[-1]+list_1[-2]+list_1[0])
    print(list_2)
    return max(list_2)


def max_harvest2(list_1):
    max_B = 0
    list_2 = []
    for i in range(len(list_1)-1):
        harvest = list_1[i-1]+list_1[i]+list_1[i+1]
        if harvest > max_B:
            max_B = harvest
        print(harvest, end="  ")
    last_harvest = list_1[0]+list_1[-1]+list_1[-2]
    if last_harvest > max_B:
        max_B = last_harvest
    print(last_harvest)
    return max_B


print('VARIANT №1:')
print(max_harvest1(berry))
print("VARIANT №2: ")
print(max_harvest2(berry))

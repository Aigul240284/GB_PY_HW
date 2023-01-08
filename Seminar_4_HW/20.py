# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
# 6 12
import random
import os
os.system('cls')
n = int(input('Input the length of the array1: '))
m = int(input('Input the length of the array2: '))


def same_numbers_in_arrays(N, M):
    array_1 = list(random.randint(1, 10) for i in range(N))
    array_2 = list(random.randint(1, 10) for i in range(M))
    print(array_1)
    array_1 = set(array_1)
    print(array_2)
    array_2 = set(array_2)
    array_3=array_1 & array_2    
    return array_3
print(same_numbers_in_arrays(n, m))


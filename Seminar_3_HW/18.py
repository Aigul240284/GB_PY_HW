import random
import os
os.system('cls')

# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

lenght_array = int(input('DZ№ 18 \n Введите длину массива: '))
array = []
for _ in range(lenght_array):
    array.append(random.randint(1, 10))
print(array)
find_num = int(input('Введите число: '))
next_num = array[0]
dif=abs(find_num-array[0])
for i in array:
    # if i== find_num: next_num=i
    if abs(i-find_num) < dif:
        dif=abs(i-find_num)
        next_num=i
print(f'ближайший элемент: {next_num}')



import random
import os
os.system('cls')
# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
# Ввод: 5
# Ввод: 1
# 1 2 1 2 2
# Вывод: 2
lenght_array = int(input('DZ№ 16 \n Введите длину списка: '))
list_1 = []
for _ in range(lenght_array):
    list_1.append(random.randint(1, lenght_array//2))
print(list_1)
num = int(input('Введите число, которое нужно найти в массиве: '))
count = 0
for i in range(0, lenght_array):
    if list_1[i] == num:
        count += 1
print(count)




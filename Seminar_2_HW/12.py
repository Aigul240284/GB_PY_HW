# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
import os
os.system('cls')


try:
    sum = int(input('TASK №12: Input the sum of the hidden numders: '))
    product = int(input('Input the product of the hidden numders: '))
    task_answer=0
    for i in range(sum):
        if i*(sum-i)==product:
            print(f'Petya quessed the numbers: {i} and {sum-i}')
            task_answer=1
            break
    if task_answer==0:
        print('These numbers are wrong, please, try again.')
        
except:
    print('Invailid input, please, try again.')
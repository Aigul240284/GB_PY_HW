tel=r'Seminar_6_HW\tel.txt'
def WriteFile():
    with open(r'Seminar_6_HW\tel.txt', 'a', encoding ='UTF-8') as data:
        data.writelines(input('Введите фамилию:'))
        data.write(' ')
        data.write(input('Введите  имя:'))
        data.write(' ')
        data.write(input('Введите отчество:'))
        data.write(' ')
        data.write(input('Введите номер телефона:'))
        data.write('\n')
        
def ReadFile():
    result=[]
    with open(r'Seminar_6_HW\tel.txt', 'r+', encoding='UTF-8') as data:
        for line in data:
            result.append(line.split())
    print(result)
    return result

def findTel(tels):         
    name=(str(input('Введите имя абонемента для поиска: ')))
    for user in tels:
        # print(tels[1])
        if user[1]==name:
            print(f"{user[1]} {user[2]} -  {user[3]}")



def deleteTel(tels):
    open(r'Seminar_6_HW\tel.txt', 'w', encoding ='UTF-8')
    name=(str(input('Введите имя абонемента для удаления: ')))
    for user in tels:
    # print(tels[1])
        if user[1]!=name:
            with open(r'Seminar_6_HW\tel.txt', 'a', encoding ='UTF-8') as data:
                data.write(user[0])
                data.write(' ')
                data.write(user[1])
                data.write(' ')
                data.write(user[2])
                data.write(' ')
                data.write(user[3])
                data.write('\n')
    ReadFile()
                

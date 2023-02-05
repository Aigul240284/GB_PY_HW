def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(' '))
            # data= result(enumerate(users))
        # print(data)
        return result
    

def save_data_to_file(name,name_inf, num, data_list2):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(name_inf)
        datafile.write(num)
        datafile.write(' ')
        datafile.write(data_list2 +'\n')


def print_bus():
    return read_data_from_file('bus.txt')

def add_bus():
    print(print_bus())
    save_data_to_file('bus.txt','bus', str(findlen_file(read_data_from_file('bus.txt'))), input("Введите государственный номер нового транспортного средства: "))
    print(print_bus())
    
def print_driver():
    return read_data_from_file('driver.txt')


def add_driver():
    print(print_driver())
    save_data_to_file('driver.txt','driver', str(findlen_file(read_data_from_file('driver.txt'))), input("Введите фамилию водителя: "))
    print(print_driver())
    
def findlen_file(tels):      
    return(len(tels)+1) 

def print_route():
    return read_data_from_file('route.txt')

def add_route():
    print(print_bus())
    bus='bus'+ input('Введите числовой порядковый номер автобуса: ')
    line=print_bus()
    for user in line:
        if user[0]==bus:
            res=user[0]
    print(print_driver())
    driver='driver'+ input('Введите числовой порядковый номер водителя: ')
    line_1=print_driver()
    for user in line_1:
        if user[0]==driver:
            res2=user[0]
    with open('route.txt', 'a', encoding='utf8') as datafile:
        datafile.write(str(findlen_file(read_data_from_file('route.txt'))))
        datafile.write(' ')
        datafile.write(res)
        datafile.write(' ')
        datafile.write(res2 +'\n')
    print(print_route())


    
    

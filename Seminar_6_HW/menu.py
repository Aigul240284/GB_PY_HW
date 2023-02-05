import function as f
menuitems = [
        ("1", "Вывод данных абонента"),
        ("2", "Вывести на экран список абонентов"),
        ("3", "Поиск номера телeфона абонента"),
        ("4", "Удаление абонента из базы")]
for i in menuitems:
        print(i[0],i[1])   
text=int(input('Введите номер: '))
if text==1: 
       f.WriteFile()
elif text==2:
        f.ReadFile()
elif text==3:
        print(f.findTel(f.ReadFile()))
elif text==4:
        print(f.deleteTel(f.ReadFile()))
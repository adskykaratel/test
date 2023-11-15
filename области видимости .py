'-------------------------------Область видимость -----------------------------------'
# Legb - local enclosed global build-in

'------------------------build - in ---------------------'

# встроенное пространство иммен (list , sum , print, input)

'-------------------------Global--------------------------------------'
 # все переменные , которые мы создали внутри одного файла
 # ЧТОБЫ  посмотреть глобальные переменф мможно испольщовать globals

a = 5
b = 6
c = 7 
# print(globals())


'------------------------enclosed (nonlocal)-----------------------'

#зАМКНУТОЕ ПРОТСТАНСТВО ИМЕН - ЛОКАЛЬНОЕ ПРОСТРАНСТВО У КОТОРОГО ЕСТЬ ВНУТРЕНЕЕ ЛОКАЛЬНОЕ ПРОСТРАНСТВО 


# var = 'global'


# def func():
#     var = 'enclosed'
#     def inner_func():
#         var = 'lacal'
#         print(var)
#     print(var)
#     inner_func()
# print(var)
# func()

'--------------------------local---------------------------'
# Локальное пространство имен - переменные , созданные внутри функции

# a = 10 
# def func(a,b):
#     print("Global", globals())
#     print('local', locals())
#     print(a,b)
# func(5,7)


# count_1 = 1

# def count1():
#     print(count_1)
# count1()




# def counter(i):
#     count_ = 0 

#     def inner_counter():
#         nonlocal count_     #доступ на изменение переменной замкнутого пространства
#         print(count_)
#         count_ +=1
#     for _ in range(i):
#         inner_counter()
# counter(10)




# open -  ффункция , которая открываеет файл в определенном режиме 

'''
Режимы :
r - read (только для чтения )
w - write(только для записи каждый разраз файл очищает )
a - append (только для добавления записи , добавляет в конец файла
х - чоздает файл если оно уже сущесьвует выйжет ошибка 
b -  binary (открывает файл в бинарном виде) 

'''



# new_fail = open('text1.txt', 'x')
# print(dir(new_fail))
# new_fail.close()




# '----------------------Read--------------------------'
# file = open ('text1.txt' , 'r')
# print(file.read())
# # print(file.writable())   # метод который проверяет можно ли что то написать в файле 

# # print(file.readable()) № метод который проверяет можно ли прочитать файл

# # print(file.read())

# # print(file.readline()) # ыфводит только строку документа возврашает строку можно использовать методы строк 
# print(file.readline(2)) #выводит только два первых символа
# print(file.readline().replace('\n',''))
# print(file.readline().replace('\n',''))
# print(file.readline().replace('\n',''))
# file.seek(0)
# print(file.readlines()) #возврашает список с элементами строки

# print(file.tell()) # смотрит расположения курсора 

# file.seek(5)

# print(file.tell())


# file.close()





'-------------------------Write--------------------------'

# file = open('text1.txt' , 'w') # очищает файл и происходит очищения 
# print(file.readable())
# print(file.writable())
# file.write('Eldos Zhantoroev')
# file.write('1\n')
# #перед тем как записать файл очишает полнсотью
# file.writelines(['bootcamp', 'Yimabek' , 'Tom'])
# # принимает список только строками
# file.close()



'------------------------------------Append-------------------------------------'
# file = open('text1.txt' , 'a') 
# print(file.readable())
# print(file.writable())
# file.write('\nAdaaaa ')

# file.close()


'------------------------`Контекстный менеджер-------------------------------'

# контрукция with работает с любыми  обьектами у которых есть два метода 
#_enter_, _exit_


# _enter_ работает в начале конструкция with (Try)


# _exit_ рфботает когда конструктор закончил работу и заканчивает конструкция через finally



# with open('text1.txt' , 'w+') as file:
#     print(file.readable())
#     print(file.writable())
#     file.write('1,2,3,4,5')
#     print(file.tell())
#     file.seek(0)
#     print(file.read())


# file = open('text1.txt' , 'w+') # очищает файл и происходит очищения 
# print(file.readable())
# print(file.writable())
# file.write('Eldos Zhantoroev')

# file.seek(0)
# print(file.read())
# file.close()

# file = open('users.txt' , 'w+') 
# print(file.readable())
# print(file.writable())
# a = input('Введите логин')
# b = int(input('Введите пароль'))
# file.write(f"""Введите логин: {a}
# Введите пароль: {b}""")
# file.seek(0)
# print(file.read())
# file.close()



# with  open('user5.txt' , 'w+') as file: 

#     s = 'aaa2 222 234 asa8'
#     length = len(s)
#     integers = []
#     i = 0  # индекс текущего символа
#     file.seek(0)
#     while i < length:
#         s_int = ''  # строка для нового числа
#         while i < length and '0' <= s[i] <= '9':
#             s_int += s[i]
#             i += 1
#         i += 1
#         if s_int != '':
#             integers.append(int(s_int))
 


# print(sum(integers))


# text = '''' Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions;
# you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2),
# but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python.
# "
# '''





# # o_words = []
# # with open('python.txt' , 'r+') as file:
# #     data = file.read().split()
    
# #     for word in data:
# #         if 'o' in word:
# #             o_words.append(word)

# # print(o_words)
# d = {'Yiman': 1, 'Eldos': 2, 'Rrr': 3}
# def print_keys():
#     for key in d:
#         print(key)
# print_keys()



# def print_argument_types(a, b):
#     a
#     print(f"Тип первого аргумента: {type(a)}")
#     print(f"Тип второго аргумента: {type(b)}")

# a = 43
# b = 'dfghjkl'
# print_argument_types(a , b)

# with open('Database.txt','a+') as file:
    # print(file.readable())
    # print(file.writable())
    # file.seek(0)
#     dic = file.readline().split()
#     print(dic)
#     database = dict(zip(dic[::2],dic[1::2]))
#     database1 = database.update(database)
#     print(database1)
#     # for line in dic:
#     #     key,value = line.split(": ")
#     #     database.update({key:value})
#     print(database)
#     def in_database(name):
#         for key,val in database.items():
#             sp =  (database['name'] == name) 
#             if sp ==True:
#                 return True
#         return False
#     def reg_database(name,password,password1):
#         if in_database(name):
#             return f'Ползователь с таким именем уже существует!'
#         if password != password1:
#             return f'Пороли не совподают'
#         user = {'name':name, 'password': password}
#         with open('Database.txt','a+') as file:
#             for key, val in user.items():  
#                 file.write(' {} {} '.format(key,val))
#         return f'Вы успешно зарегистрировались'
#     def login(name,password):
#         if not in_database(name):
#             return f"Пользователь не найден"
#         for user in database:
#             sp =  (database['name'] == name) 
#             if sp ==True:
#                 sd = (database['password'] != password)
#                 if sd == True:
#                     return 'Пароль не найден'
#         return 'Вы успешноо вошли!'
#     def main():
#         print('Добро пожаловать')
#         while True:
#             action = input("Введите чтото из этого -> register:1, login:2, quit:3, Просмотр базы: 4  ")
#             if action == '3':
#                 break
#             elif action == '1':
#                 name = input("Введите имя пользователья: ")
#                 password = input("Введите пароль: ")
#                 password1 = input('Введите пароль снова: ')
#                 print(reg_database(name,password,password1))
#             elif action == '2':
#                 name = input("Введите имя пользователья: ")
#                 password = input('Введите пароль: ')
#                 print(login(name,password))
#             elif action == '4':
#                 print(database)
#             else:
#                 print('Не корректный выбор')
# main()

# def load_database(filename='Database.txt'):
#     try:
#         with open(filename, 'r') as file:
#             data = file.read().split()
#             database = dict(zip(data[::2], data[1::2]))
#         return database
#     except FileNotFoundError:
#         return {}

# def save_database(database, filename='Database.txt'):
#     with open(filename, 'w') as file:
#         for key, value in database.items():
#             file.write(f'{key} {value} ')

# def in_database(database, name):
#     return name in database

# def reg_database(database, name, password, password1):
#     if in_database(database, name):
#         return 'Пользователь с таким именем уже существует!'
#     if password != password1:
#         return 'Пароли не совпадают!'
#     database[name] = password
#     save_database(database)
#     return 'Вы успешно зарегистрировались!'

# def login(database, name, password):
#     if not in_database(database, name):
#         return 'Пользователь не найден!'
#     if database.get(name) != password:
#         return 'Пароль не найден!'
#     return 'Вы успешно вошли!'

# def main():
#     database = load_database()
#     print('Добро пожаловать!')
#     while True:
#         action = input("Введите одно из следующих действий: register - 1, login - 2, quit - 3, Просмотр базы - 4: ")
#         if action == '3':
#             break
#         elif action == '1':
            # name = input('Введите имя пользователя: ')
#             password = input('Введите пароль: ')
#             password1 = input('Введите пароль еще раз: ')
#             print(reg_database(database, name, password, password1))
#         elif action == '2':
#             name = input('Введите имя пользователя: ')
#             password = input('Введите пароль: ')
#             print(login(database, name, password))
#         elif action == '4':
#             print(database)
#         else:
#             print('Некорректный выбор!')

# if __name__ == '__main__':
#     main()

def err():
    try:
        print('5'+5)
    except TypeError:
        print('Type что ли')
# err()

def n():
       with open('text.txt','w+') as file:
        a = "123435a"
        file.write(a)
        file.seek(0)
        b = file.read()
        s = []
       try:
            p = map(int,b)
            s.append(list(p))
            print(list(s))
       except ValueError:
              print('Ошибка значения!')
       finally:
              print(s)
# n()


# with open('text12.txt','w+') as file:
#     a = input('')
#     file.write(a)
#     file.seek(0)
#     b = file.read()
# def proverka():
#       for i in b:
#             if "w"in b:
#                   print('Да, в тексте есть w')
#                   break
#             else:
#                   print('Нет, в тексте нет w')
#                   break
# proverka()




# '-----------------------------Try Except---------------------------------------'
# # Исключения это обьекты которые прерывают работу кода, если не были
# # обработаны (связаны с логикой программы)


# # print('Yello')
# # try:
# #     print(5/0)
# # except ZeroDivisionError:
# #     print('На ноль делить нельзя')


# # Ошибки - обьекты которые прервывают работу и  их нужно  обработать (связаны по большой части с разработчиком )


# '''
# SyntaxError : unexcepted E0F while paarsing
# (Когда мы не закрыли скобку либо кавычку) 

# a = 
# SyntaxError: invalid syntax
# (Когда мы сделали что - то не правильноев синтаксисе)

# '''

# NameError
# # исключения , которое выходит когдма мы обращаемся к несуществуещей переменной


# ''''
# nam3_1 = 'str'
# print(name_2.islower())
# NameError : name'name_2' is not defined
# '''
# IndexError
# # исключения , которые выходит когда мы обращаемся по несуществующему индексу

# '''
# list_ = [1,2,3,4,5]
# list_[50]
# IndexError: list index out of range


# [1,2,3].pop(5)
# IndexError: list index out of range
# '''

# KeyError
# # исключения , которые выходит когда мы обрашемся по несууществуешему ключу

# '''
# dict_ = {'a','1'}
# dict_['b']
# KeyError: 'b' 
 
# dict_ = {'a':1}
# dict_get('b') None


# '''

# ValueError
# # исключения, когда мы передаем в функцию не коректный для нее тип данных

# # когда мы распаковываем итерируемый обьект на несколько переменных и количевство переменных не совпадает с количеством элементов внутри итериуемого обьекта 
# '''
# int('10b')
# ValueError : invalid literal for int() with base 10: '10b'
# '''




# TypeError
# # исключения, когда мы пытаемся использовать методы не свойственные какому- то типу данных или когда мы пытаемся передать функции больше или
# #  меньше аргументов , чем принимаем функции

# '''
# for i in 55:
# TypeError: 'int' object in not iterable'''
# '''
# 5+'5'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# '''

# AttributeError
# # выходит когда мы обращемся к несуществуешему методы или атрибуту обьекту данных 
# '''
# [].replace('a','')
# AttributeError: 'list' object has no attribute 'replace'

# '''

# IndentationError
# # выходит когда мы нне правильно используем отступы 


# '''for i in 50:

# IndentationError: expected an indented block after 'for' statement on line 98'''




# Exception
# # исключения которые создали с ами чтобы его вызвать 

# raise Exception('Моя ошибка')




# '------------------------Вызов исключении-----------------------------------'

# # raise SyntaxError

# import math
# result = math.sqrt(11 **3 - 8**3) / (math.factorial(6)*math.pi)
# print(result)




# a = int(input("Введите значение a: "))
# b = int(input("Введите значение b: "))
# c = int(input("Введите значение c: "))

# D = b**2 - 4*a*c

# if D > 0:
#     x1 = (-b + D**0.5) / (2*a)
#     x2 = (-b - D**0.5) / (2*a)
#     print("Два корня:")
#     print("x1 =", x1)
#     print("x2 =", x2)
# elif D == 0:
#     x1 = -b / (2*a)
#     print("Один корень:")
#     print("x1 =", x1)
# else:
#     print(" Дискриминант меньше нулья")





# import math

# #  для вычисления длины окружности
# def c(radius):
#     return 2 * math.pi * radius

# # для вычисления площади круга
# def d(radius):
#     return math.pi * radius ** 2

# choice = input("Введите 'R' для ввода радиуса или 'D' для ввода диаметра: ")

# if choice == 'R' or choice == 'r':
#     radius = float(input("Введите радиус круга: "))
# elif choice == 'D' or choice == 'd':
#     diameter = float(input("Введите диаметр круга: "))
#     radius = diameter / 2
# else:
#     print("Неверный выбор. Пожалуйста, введите 'R' или 'D'.")
#     exit()

# # Проверка на положительность радиуса
# if radius <= 0:
#     print("Радиус должен быть положительным числом.")
# else:
#     circumference = c(radius)
#     area = d(radius)
#     print(f"Длина окружности: {circumference}")
#     print(f"Площадь круга: {area}")










# def load_database(filename='Database.txt'):
#         try:
#             with open(filename, 'r') as file:
#                 data = file.read().split()
#                 database = dict(zip(data[::2], data[1::2]))
#             return database
#         except FileNotFoundError:
#             return {}

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
#             name = input('Введите имя пользователя: ')
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






'------------------------------Обработка исключении-----------------------------------'

# Чтобы код не прекращал свою работу , мы можем использовать конструкцию try-except  и оброботать вызванное исключение

# try:
#     #код который возможно вызовет ошибку 
#     num = int(input('Введите число'))
# except ValueError: # исключения, который может возникнуть 
#     print('Вы ввели не чсило!')
# else: #код который отработает только если никакая ошибка не вызвалась
#     print('Вы ввели число ,', num )
# finally: #код который отработает в любом случае
#     print('Финал')






# try:
#     num = int(input("введите число"))
#     if num ==0:
#         raise ValueError
# except ValueError:
#     print("Вы ввели ноль")



# try:
#     a = int(input())
#     k = 10/a
#     raise Exception
# except:
#     print('Отлавлена любая ошибка')



# try:
#     raise TypeError('Моя ошибка')
# except TypeError as error:
#     print(error)




# try:
        # num1 = int(input())
        # num2 = int(input())
        # print(num1+num2)
# except ValueError:
#         print('Введите число ')

# a , b = 1, 0 
# try:
#     print(a/b)
#     print('Это сообщения не будет напечатано')
#     print(10+'10')
# except TypeError:
#     print('Вы сложили значения несовместимых типов ')
# except ZeroDivisionError:
#     print('Деления но 0')


# try:
#     print(a/b)
# except:
#     print("Длеления на ноль")
# print('будет ли это сообшениянапечатано')



# try:
#     print('1'+1)
#     # print(name)
#     # print(1/0)
# except NameError:
#     print("Name не существует")
# except ZeroDivisionError:
#     print('Деления на ноль')
# except:
#     print('Xnj nj gjikj yt nfr')




'-------------------------------Assert (Утверждения)----------------------------------------------------'



# a = 1 
# assert a ==0, 'Сообщения об ошибке'
# print(a)




# def divivde():
#     try:
#         num1 = int(input())
#         num2 = int(input())
#         print(num1/num2)
#     except ZeroDivisionError:
#         print('Нельзя поделить но 0')
#     except ValueError:
#         print('Можно делить только на цифры')
# divivde()

# from calculator import add,substract

# a = add(5,10)
# print(a)

# a = substract(5,10)
# print(a)
# 
# import os

# pwd = os.getcwd()
# print ("Текущяя директория", pwd)




# ls = os.listdir
# print(ls)

#os.mkdir('Новая папка')






# from hello import hello

# name = 'Anton'

# print(hello(name))


# from my_pacage import calculator

# print(calculator.add(5,5))
# Функция это именнованный блок кода которая вызывается множества раз в других частях программы.
# Параметры функции это переменные которые будут принимать вага функция, для того, чтобы вы смогли работать с данными, которые попадают в вашу функцию 
# аргументы -  данныекооторые мы передаем для параметра при вызове функции



# string = 'abcdef'
# def our_len(str):
#     count = 0
#     for i in str:
#         count+=1
#     return count
# print(our_len(string))



'------------------------------------------------Виды аргументов------------------------------------------------------'
#Позиционные аргументы
#  (передаются в параметры по позиции)
# Именнованные аргументы (Передаются по названию параметр = значения)



# def sum_(num1 , num2):
#     res = num1 + num2
#     return res
# print(sum_(5))




# def sum_(num1 , num2=5):
#     res = num1 + num2
#     return res
# print(sum_(5,1))





#Аргументы быво=ают обязательными и необязательными
'''
Обязательные - это те аргументы которым при вызове функции должны передоваться значения
необязательные - это аргументы которые не требуют значения при вызове функции
так как при создании функции мы указываем значения по умолчанию
'''


#При распоковке картежа , списка и множества мы используем одну *
# При распоковке словаря мы используем **


# list1 = [1,2,3,4,5]
# print(*list1)
# dict1 = {'a':1, 'b':2, 'c':3}
# print(dict1)
# dict2 = {**dict1, 'f':4}

# print(dict2)



'------------------------------------------Произвольнве аргументы--------------------------------------------------------'


# Произвольные количество аргументов используется когда нам заранее неизвестно количества аргументов 
#  *args - данные передаются ввиде tuple
# **kwargs - данныее передаются ввиде dict (словаря)

# def sum_(num1,num2=0,*args):
#     res = num1 + num2
#     print(type(args))
#     if args:
#         for i in args:
#             res+=i
#     return res
# print(sum_(1,2))
# print(sum_(1,2,3,4,5,6,7,8,9))
# print(sum_(1))




# def great(*args):
#     for name in args:
#         text = f"Hello {name}"
#         print(text)
# great('Eldos','Men','Sen')





'----------------------------------------ввиды параметров --------------------------------------------'
#Обязательные
# Необязательные 
        # С дефолтом значения (по умолчанию)
        # args (все позиционные аргументы , которые не попали в обязательные )
        #  kwargs (все лишние именования  параметры )






# # Функция для сложения
# def add(x, y):
#     return x + y

# # Функция для вычитания
# def subtract(x, y):
#     return x - y

# # Функция для умножения
# def multiply(x, y):
#     return x * y

# # Функция для деления
# def divide(x, y):
#     if y == 0:
#         return "Деление на ноль невозможно"
#     return x / y

# while True:
#     print("Выберите операцию:")
#     print("1. Сложение")
#     print("2. Вычитание")
#     print("3. Умножение")
#     print("4. Деление")
#     print("5. Выйти")

#     choice = input("Введите номер операции (1/2/3/4/5): ")

#     if choice == '5':
#         print("Программа завершена.")
#         break

#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Введите первое число: "))
#         num2 = float(input("Введите второе число: "))

#         if choice == '1':
#             print("Результат:", add(num1, num2))

#         elif choice == '2':
#             print("Результат:", subtract(num1, num2))

#         elif choice == '3':
#             print("Результат:", multiply(num1, num2))

#         elif choice == '4':
#             print("Результат:", divide(num1, num2))
#     else:
#         print("Неверный ввод")




# '------------------------lambda-------------------------'
# # lambda - анонимная функция , которая записовает в одну строку 
# lambda_func = lambda x : x**2
# print(lambda_func(5))

# calcular = {
#     '+': lambda n1,n2 :n1 + n2,

#     '-': lambda n1,n2 :n1 - n2,

#     '*': lambda n1,n2 :n1 * n2,

#     '/': lambda n1,n2 :n1 / n2,

#     '//': lambda n1,n2 :n1 // n2,

#     '**': lambda n1,n2 :n1 ** n2,

#     '%': lambda n1,n2 :n1 % n2,
# }
# def main():
#     num1 = int(input('Введите число №1'))
#     num2 = int(input('Введите число №2'))
#     oper = input('Знак')
#     func = calcular[oper]
#     res = func(num1,num2)
#     sam = func(num1,num2, '=',res)
# main()







'-----------------------------------Registr , login------------------------------------------------'
database = [
    {'name' : 'Anton', 'password' : 12345},
]

def in_database(name):
    for user in database:
        if user['name'] == name:
            return True
    return False
def reg_database(name,password1,password2):
    if in_database(name):
        return f'Юзер с таким именем не существует!'
    if password1 != password2:
        return f'Пароли не совпадают'
    user = {'name': name, 'password':password1}
    database.append(user)
    return f'Вы успешно зарегистрировались'

def login(name,password):
    if not in_database(name):
        return'Пользователь не найден'
    for user in database:
        if user['name'] == name:
            if user['password'] != password:
                return "Пароль неверный"
    return 'Вы успешно вошли'

def main():
    print('Добро пожаловать ')
    while True:
        action = input("Введите что то из этого -> register:1 , login:2, quit:3")
        if action =='3':
            break
        elif action =='1':
            name = input("Введите имя пользователья ")
            password1 = input("Введите пароль: ")
            password2 = input("Введите пароль снова :")
            print(reg_database(name,password1,password2))
        elif action =='2':
            name = input("Введите имя пользователья ")
            password1 = input("Введите пароль: ")
            print(login(name,password1))

        else:
            print('Не коректный выбор!')
# main()

# from human import eat

# # print(eat('Banan'))

# from human import animal

# print(animal('Cow'))

def divide():
    try:
            num1 = int(input("Введите число №1: "))
            num2 = int(input("Введите число №2: "))
            print(f'{num1} / {num2} = {num1/num2}')
    except ZeroDivisionError:
            print("На ноль разделят нельзя!")
            divide()
    except ValueError:
            print("Введите только число!")
            divide()
    else:
            print('Без ошибок')
# divide()




# with open('texterror.txt','w') as file:
#        a = input("Введите текст!")
#        file.write(a)
def my_file():
    try:
           with open('texterror.txt','r+') as file:
                  file.seek(0)
                  print(file.read())
                  file.seek(0)
                  s = file.read()
                  print(s)
    except FileNotFoundError:
            print("Такого файла не существует!")
    except FileExistsError:
           print("ХЗ что за проблема!")
# my_file()




def er():
       try:
              print('5'+5)
       except TypeError:
              print("TypeError")
# er()


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
#     # a = input('')
#     file.write(a)
#     file.seek(0)
#     b = file.read()
# def proverka():
#       for i in b:
#             if "w" in b:
#                   print('Да, в тексте есть w')
#                   break
#             else:
#                   print('Нет, в тексте нет w')
#                   break
# proverka()

# def css():
#     name, contry,year = input('Введите имя, страну, год рождения, через пробел: ').split() 
#     year = int(year)
#     print(name,contry,year)
# # css()



# def dic(dict1):
#     try:
#           print(dict1.get('name'))
#           print(dict1.get('age'))
#     except KeyError:
#           print("KeyError")
# dic(dict1={'name':input("Имя"), 'age': input("Возраст")})
          


# def l():
#     l1 = [2, 3, 0, 1]
#     l2 = [10, 20, 30, 40]
#     l3 = []
#     for i in l1:
#           l3.append(l2[i])
#     print(*l3)
# # l()

# a = int(input('Введите число №1'))

# b = int(input('Введите число №2'))

# c = int(input('Введите число №3'))

# qwe = lambda : a*b*c
# print(a*b*c)

# s = lambda a,b : a**3+b**3
# print(s(12,15))


# def Kakashi(a):
#      if a % 2 ==0:
#         return a 
#      else:
#         return Kakashi(a-1)
# Kakashi(999)




# new = lambda days:  f'Оставлось дней до нового года{365 - days} '

# print(new(int(input('Введите количество дней с нового года'))))


# age = lambda old:f'Вам вот столько дней{old*365}'
# print(age(int(input('Введите сколько вам лет'))))

# def rec(): 
#     a = [1,2,3,4,5,6]
#     if a == 0:
#         return  a
#     a =a[:-1]

#     print(a)   
    
# rec()

# a =  [2, 5, 20, 100, 9, 1, 6, 7, 12, 8 ]
# b = list(map(lambda c: c**2,a))
# print(b)



# d =  [2, 5, 20, 100, 9, 1, 6, 7, 12, 8 ]
# w = list(filter(lambda c: (c%3==0),d))
# print(w)
# 'Камень-Ножницы-Бумага с Компьютером'
# def ch(choi):
#     import random
#     cm_choice = ['Камень','Ножницы','Бумага']
#     rand = random.choice(cm_choice)
#     if choi == rand:
#         print('Invalid')
#         print(f'Your choice: {choi}')
#         print(f'Comp choice: {rand}')
#     elif (choi == 'Камень' and rand == 'Ножницы') or (choi == 'Ножницы' and rand == 'Бумага') or (choi == 'Бумага' and rand == 'Камень'):
#         print("You win")
#         print(f'Your choice: {choi}')
#         print(f'Comp choice: {rand}')
#     else:
#         print("Не сегодня бро")
#         print(f'Your choice: {choi}')
#         print(f'Comp choice: {rand}')
#     return game()
# def game():
#     while True:
#         choice = input('Ваш выбор: Камень|1, Ножницы|2, Бумага|3 Выход|4   : ')
#         if choice == '1':
#             stone = "Камень"
#             print(ch(stone))
#         if choice == '2':
#             scissor = 'Ножницы'
#             print(ch(scissor))
#         if choice == '3':
#             paper = 'Бумага'
#             print(ch(paper))
#         if choice == '4':
#             print("Вы покинули игру!")
#             break
# # game()


# def sum_f(number):
#      if n  == 0 :
#           return 0 
#      else:
#           res = number %10 + sum_f(number//10)
#           return res  
     


# def rec(n):
#     if n==0:
#         return 0
#     else:
#         res = n % 10 + rec(n//10)
#         return res
# n = int(input("Введите число: "))
# print(f'Сумма равна {rec(n)}')



# def my_(name):
#      print(f'hello{name}')
# you_ = my_
# you_('Eldos')





# def nee_function(func):
#      print('Я функция которая принимает другую функцию')
#      func('Python')
#      print('коонец')
# you_(my_)



'--------------Декораторы---------------------------------'
#  Функция высщего порядка - эта та функция которая 
# принмает в аргументы функции , создает внутри себя  
# функции, вывзает функцию и возвращает функцию


# def func1(func):
#      print(func())
#      return func

# def func2():
#      print('Hello')
#      return ' Bye'
# func1(func2)




# Декораторы - это функция высшего порядка , которая нужна 
# чтобы расширить функционал другой функции не изменяя ее (функция обвертка)







def naruto(kurama):
    def konoha(*args,**kwargs):
          from datetime import datetime
          print('start:',datetime.now())
          kurama(*args,**kwargs)
          print('finish:',datetime.now())
    return konoha


# def hello():         #первый способ вызова декоратора 
#     print('Hello world')
# func1=naruto(hello)
# func1()


# @naruto               # второй способо вдальнейшем будемиспользовать тюк более удобнее
# def hello():
#     print('hello world')
# hello()




# @naruto
# def func_():
     
#  '''
# это функция ничего не принимает и возвращает None
# '''
# pass

# print(func_.__doc__)
# print(func_.__name__)


# def dec(fun):
#     def wrap(*args, **kwargs):
#         a = fun(*args, **kwargs)
#         return a ** 2
#     return wrap

# @dec
# def num(a, b):
#     return(a + b)

# print(num(2,2))

# def decorator(num):
#     def inner_decarator(func):
#         def wrapper(*args,**kwargs):
#                for i in range(num):
#                     func(*args,**kwargs)
#         return wrapper
#     return inner_decarator 
     
# @decorator(5)
# def sum_(a,b):                              1
#     print(a+b)
# sum_(5,10)



# inner_decarator = decorator(5)
# wrapper = inner_decarator(sum_)                       2
# wrapper(5,10)



# decorator(5)(sum_)(5,10)                              3




# import random
# from datetime import datetime, timedelta

# def generate_death_date(birth_date):
#     # Преобразуем введенную дату рождения в объект datetime
#     birth_datetime = datetime.strptime(birth_date, "%Y-%m-%d")

#     # Добавляем 18 лет к дате рождения
#     adulthood_datetime = birth_datetime + timedelta(days=18 * 365)

#     # Генерируем случайное количество дней после достижения 18 лет (от 1 до 36525, что соответствует 100 годам)
#     random_days = random.randint(1, 36525)

#     # Создаем объект timedelta с сгенерированным количеством дней
#     death_timedelta = timedelta(days=random_days)

#     # Вычисляем дату смерти, добавляя timedelta к дате достижения 18 лет
#     death_datetime = adulthood_datetime + death_timedelta

#     return death_datetime.strftime("%Y-%m-%d")

# # Получаем дату рождения от пользователя
# birth_date = input("Введите дату рождения в формате YYYY-MM-DD: ")

# # Генерируем и выводим дату смерти после 18 лет
# death_date = generate_death_date(birth_date)
# print(f"Дата смерти после 18 лет: {death_date}")
 



# def random_ch(func):
#     def upper_case(*args,**kwargs):
#         ran = func(*args,**kwargs)
#         return ran.upper()
#     return upper_case

# @random_ch
# def r(list_):
#     from random import choice
#     rand = choice(list_)
#     return rand
# lisl1 = ['yimanbek','18',"future", "devops","engineer"]
# print(r(lisl1))

# def mult(fun):
#     def wrap(*args,**kwargs):
#         ml = fun(*args,**kwargs)
#         return ml ** 2
#     return wrap
# @mult
# def mul(a,b):
#     return a*b
# print(mul(2,2))

# import random

# def num(numbers):
#     def chislo(*args, **kwargs):
#         result = numbers(*args, **kwargs)
#         return list(set(result)) 
#     return chislo

# @num
# def random_num():
#     return [random.randint(10, 50) for _ in range(100)]

# random_numbers = random_num()
# print(random_numbers)




# def decorator(func):
#     def wrapper(*args,**kwargs):
#         login = input('Введите логин: ')
#         passpword = input("Введите пароль: ")
#         new_login = ''.join(chr(ord(char)+1) for char in login)
#         new_password = ''.join(chr(ord(char)+1) for char in passpword)
#         return func(new_login,new_password)
#     return wrapper

# @decorator
# def glavnyi(login,password):
#     print(f'Ваш зашифрованный логин: {login}')
#     print(f'Ваш зашифрованный пароль: {password}')

# glavnyi()
# print(chr(ord('a')+5))


# def decorator(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#         func(*args,**kwargs)        
#     return wrapper

# @decorator
# def mult(n1,n2):
#     print(n1*n2)
# mult(2,5)
# mult(5,8)


def header(func):
    def wrapper(*args,**kwargs):
        print('<h1>')
        func()
        print('</h1>')
    return wrapper


def adam(func):
    def wrapper(*args,**kwargs):
        print('<table>')
        func()
        print('</Table>')
    return wrapper


# # @adam
# # @header
# def hello():
#     print('Hello world')
# # hello()




# adam(header(hello))()
# # header1 = header(hello)
# # header1()





def make_bold(func):
    def wrapper(*args,**kwargs):
        print('<b>')
        func()
        print('</b>')
    return wrapper


def make_italic(func):
    def wrapper(*args,**kwargs):
        print('<i>')
        func()
        print('</i>')
    return wrapper


def make_underline(func):
    def wrapper(*args,**kwargs):
        print('<u>')
        func()
        print('</u>')
    return wrapper

# @make_bold
# @make_italic
# @make_underline
# def hello():
   
#     print('Hello world')
#     return 'Hello world'
    
# print(hello())



# def make_bold(func):
#     def wrapper():
#         return "<b>" + func() + "</b>"
#     return wrapper

# def make_italic(func):
#     def wrapper():
#         return "<i>" + func() + "</i>"
#     return wrapper

# def make_underline(func):
#     def wrapper():
#         return "<u>" + func() + "</u>"
#     return wrapper

# @make_underline
# @make_italic
# @make_bold
# def привет():
#     return "Hello world"

# print(привет())



def decorator(func):
    def wrapper(*args,**kwargs):
        login = input('Введите логин: ')
        passpword = input("Введите пароль: ")
        new_login = ''.join(chr(ord(char)+1) for char in login)
        new_password = ''.join(chr(ord(char)+1) for char in passpword)
        return func(new_login,new_password)
    return wrapper


# def databases(func):
#       def wrapper(*args,**kwargs):
#             with open('database.txt','w+') as file:
#                     file.seek(0)
#             return wrapper
      

# def read_decorator(func):
#     def wrapper(*args,**kwargs):
#         with open('database.txt','w+') as file:
#            file.read

            
# @decorator('database.txt')
def glavnyi(login,password):
    print(f'Ваш зашифрованный логин: {login}')
    print(f'Ваш зашифрованный пароль: {password}')

glavnyi()
# decorator()
# print (chr(ord('a')+5)
       
# @read_decorator('database.txt')
def login_pass():
    print(f'Ваш логин: {login}')
    # print(f'Ваш пароль: {password}')
print(login_pass())







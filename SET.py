'-----------------------------------------------Множества (set)----------------------------------------------------------------'

# множества - это изменяемый , неупорядночный , итерируемый , неиндексируемый тип данных , предназнаачем для храненияуникальных значении (нельзя хранить неизменяемые типы данных)
# даже нельзя хранить данные в tuple([1,2,3])
# Typeror unhashble



# set_1 = {1,2,3,4,5, 'ads' , 'dsf' , (1,2,3,4)}
# print(set_1)





# # set_2 = {1,1,1,1,1,1,1,1} #set хранит только уникальные значения
# # print(set_2)


# # set_3 = {True, False,0,1}  #берет значения по очередности и выведет False and True
# # print(set_3)




# '---------------------------------Методы множества ------------------------------'
# # set1 = {'1','2','3', '4'}


# # #pop -  удаляет случайный элемент из множества 
# # a = set1.pop()
# # print(a)



# # #remove - удаляет элемеНТ ИЗ СЕТ ПО ЗНАЧЕНИЮ ЕСЛИ ЭЛЕМЕНТА НЕТУ В МНОЖЕСТВЕ ВЫВОДИТ ОШИБКУ keyterror
# # set1.remove('4')
# # print(set1)


# # set1.add(4)   #add - добавляет элемент в сет 
# # print(set1)


# # # difference -  находит различие между множествомо и другой коллекцией
# # set1 = {1,2,3}
# # set2 = {3,4,5}
# # print(set1.difference(set2)) #{1,2}
# # print(set2.difference(set1)) #{4,5}




# # # symmetric_difference - находит разные значение в множествах 
# # print(set1.symmetric_difference(set2)) #{1,2,4,5}




# # # intersection - выводит одинаковые значения коллекции
# # print(set1.intersection(set2))


# # #update - добавляет все элементы итерируемого обьекта в set
# # set1 = {1,2,3}
# # set1.update('aasda')
# # print(set1)


# # #discard -  удаляет элемень по значению если в множестве не нашелся элемент не  выводит ошибку KEYerror

# # set1.discard('3')

# # #clear - очишает множество 


# # set1.clear()
# # print(set1)




# spisok = [1,2,3,4,1,1,2,3,4,5,6,7,2,'a','a','a']
# print(list(set(spisok)))






# # # dict - это изменяемый итерируемый неупорядочный неиндексируемый тип данных предназначенный для хранения данных в парах (ключ : значения)  (key:value)

# user = {'name' : 'Eldos' , 'login' :'2004' , 'password' : 'qwerty'}
# # print(user['password'])
# # print(user)


# #ключами  в словаре могуть быть только неизменяемые типы данных 
# # ключи должны быть уникальными не должны повторятся если же они повторяются сохранится последнии


# user = {'name' : 'Eldos' , 'login' :'2004' , 'password' : 'qwerty' , 'login' :'2004'}
# # print(user['login'])



# # #знаяени могут быть любые типы данных могут повторятся 

# # dict_1 = {1:'a',  2:'b' , 3:'c'}
# # print(dict_1[4])   # keyerror ошибка




# '--------------------------------------------Создания словаря---------------------------------------------'

# dict_1 = {1:'a',  2:'b' , 3:'c'}
# dict_2 = dict([(1,'a'), (2,'b') , (3,'c')])
# dict_3 = {}
# dict_3 ['name'] = 'Jhon'
# dict_3['login'] = 'Snow'
# print(dict_3)




# '-----------------------------------Методы словарей----------------------------------------'
# dict_1 = {1:'a',  2:'b' , 3:'c'}
# # get - метод который возвращает значения по ключу если такого ключа нет то возвращает None либо дефолтное значения 

# print(dict_1.get(1 , 'Такого юзера нету '))

# # pop - метод который удаляет пару по ключу и возвращает значения 
# name = user.pop('name')
# print(name)
# print(user)


# #popitem - мутод который удаляет последнию пару и возвращает ее 
# remove_ = user.popitem()
# print(remove_)

# #update - метод который расширяет словарь парами из второго словаря 
# dict1 = {1 : 'a', 2:'b' , 3:'c'}
# dict2 = {4 : 'e'}
# dict1.update(dict2)
# print(dict1)





# # clear - метод очищает словарь

# # fromkeys - метод который создает словарь новыйы словарть используя список ключей
# dict_1 = dict.fromkeys(['Anton' , 'Alina' , 'Aman', 1,2,3,4] , 'значения')
# print(dict_1)





'''
keys , values , items
- keys - метод который возвращает ключи
- values - метод который возвращает все значения 
- items -  мутод который возвращает тьюплс с ключами и значениями
'''
''

# user = {'name' : 'Eldos' , 'login' :'2004' , 'password' : 'qwerty'}
# print(user.keys())
# print(user.values())
# print(user.items())

# ''




# '----------------------------------------Итерирования словарей-------------------------------------------------------------'

# user = {'name' : 'Eldos' , 'login' :'2004' , 'password' : 'qwerty'}

# for key in user.keys():
#     print(key)


# for values in user.values():
#     print(values)




# for items in user.items():
#     print(items)





# for key, values in user.items():
#     print(key , values)

# dict_={}
# for key, values in user.items():
#     dict_[ values] = key
#     print(dict_)



university = {'Программирование' : 500,'Экономика' : 300,'Медицина' : 400}

university['Программирования'] = 400

a = {'Лингвистика': 200} 
university.update(a)
university.pop('Медицина')

for items in university.items():
    print(items)
print(university)






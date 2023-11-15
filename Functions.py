#map , filter , zip , enumerate

# zip -  соединает несколько последовталеьностой (получаем генератор в котороом элементы - tuple)


list1 = [1,2,3,4,5,6]
list2 = ['a','b','c']
list3 = [1.2,1.3,1.4]

zipped = zip(list1,list2,list3)
for a in zipped:
    print(a)

dict_ = dict(zip(list2,list3))
print(dict_)

#enumarate - нумерует последовательность (по дефолту с 0)стак же получаем генератор

enumerate = enumerate('World be like')
print(list(enumerate))


#map -  функция высшего порядка принимает другую функциюи итерирует обьект выполняет заданную функцию на каждый элемеент последовательность

# list1 = ['1','2','3']
# mapped = map(int,list1)
# print(list(mapped))

# number = map(int, input('Введите число через пробел').split())

# #split - пробел
# print(f'Summ numbers = {sum(list(number))}')



# filter - функция высшего порядка возвращаающая генератор с элементами прошедшим фильтром (какое- то условие) принимает функцию и последовательность 
list1= [1,2,3,-3,-2,-1,0]
filtered = filter(lambda x : x>0, list1)
print(list(filtered))


# string = input('Введите список слов').split()
# # result = list(map(len, string))
# # print(string)

# # print(result)


# res = [len(i) for i in string]
# print(res)


nums = [1,1,2,3,5,8,13,21,34,55,89]
nums1 = [234,55,89]
# # res = filter(lambda i : i<5, nums)
# # print(list(res))
# # res = [i for i in nums if i<5]
# # print(res)



# def find_even(spisok_chisel_na_proverku):
#     for num in spisok_chisel_na_proverku:
#         if num % 2 == 0 :
#             print(num)
# find_even()





'--------------------------------------------Функция -------------------------------------------------------------'






# table = [[0]* 5 for _ in range(5)]
# for i in range(1,6):
#     for j in range(1,6):
#         table[i -1] [j -1] = i*j
# for row in table:
#     print(row)



# #  table.append([','])
# #       table.append(['*'])

# table = [64 for _ in range(64)]
# for i in range(1,32):
#     for j in range(1,32):
#     #  i([','])
#     #  j(['*'])
# for row in table:
#     print(row)


n = 8
m = 8
chess_board = []
for i in range(n):
    row =[]
    for j in range(m):
        if(i+j) % 2 ==0:
            row.append('.')
        else:
            row.append('*')
    print(row)
    chess_board.append(row)

for row in chess_board:
    print(''.join(row))
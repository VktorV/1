# 2 Задача1
# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. Ваша задача - 
# # определить минимальное количество монеток, которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.
# n= int(input("введите число монет: "))
# from random import randint
# a, b= 0, 0
# for i in range(n):
#     temp= randint(0,1)
#     print(temp, end=" ")
#     if temp > 0: a=+1
#     else: b +=1
# print()
# if a>b:
#  print(f"нужно повернуть {b} монет")
# else:
#  print(f"нужно повернуть {a} монет")


                                    #2 задача2
#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
#Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
#Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные

# s= int(input("введите сумму чисел:")) 
# p= int(input("введите произведение:")) 
# a=0
# for x in range(s):
#     for y in range(s):
#         if x+ y == s and x*y==p:
#             a+=1
#             print(x,y)


                              #2 Задача3
#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.
# n=int(input("введите число n:"))
# k= 0
# res=1
# while res < n+1:
#  print(res, end=" ")
#  k+=1
#  res= 2**k



                            #3 задача1
#Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# import random
# N = int(input('Введите размер массива N: '))
# X = int(input('Введите число X: '))
# N_array = []
# for i in range(N):
#     N_array.append(random.randint(0, N//2))
# print(N_array)
# print(f'Число вхождений посчитали с помощью встроенной функции count {N_array.count(X)}')



                            # 3 задача2
 # Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# n = int(input())
# list_1 = list()
# x = int(input())
# for i in range(n):
#     list_1.append(x)

# k = int(input())
# m = abs(k - list_1[0]) 

# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)


                            # 3 задача2
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# dict_with_letter = {1: ("А","Е","В","И","Н","О","Р","С","Т", 
#  'A','E','I','O','U','L','N','S','T','R'), 
#  2: ("Д","К","Л","М","П","У", 
#  'D', 'G'), 
#  3: ("Б","Г","Ё","Ь","Я", 
#  'B','C','M', 'P'), 
#  4: ("Й","Ы", 
#  'F', 'H', 'V', 'W', 'Y'), 
#  5: ("Ж","З","Х","Ц","Ч", 
#  'K'), 
#  6: ("Ш", "Э","Ю", 
#  'J','X'), 
#  7: ("Ф","Щ","Ъ", 
#  'Q','Z') 
#  } 
 
# def dicting(dict_with, words): 
#  sum_points = 0 
#  for key, value in dict_with.items(): 
#   for letter in words.upper(): 
#    if letter in value: 
#     sum_points += key 
#  print(sum_points) 
# word = str(input()) 
# dicting(dict_with_letter,word)
                                     


                                              #8. телефонная книга
# '''1. Создание файла
# - открываем файл на дозапись
# 2. Внесение данных
# - получить от пользователя контактные данные
# - открываем файл на дозапись
# - записываем данные
# 3. Вывод данных на экран
# - открываем файл на считывание
# - получаем данные из файла
# - выводим данные на экран
# 4. Поиск контакта
# - запрос варианта поиска контакта
# - получить от пользователя данные для поиска
# - открываем файл на считывание
# - получаем данные из файла
# - осуществляем поиск контакта
# - выводим контакт на экран
# 5. Создание интерфейса
# - выводим меню пользователя на экран
# - запрос действия
# - запуск соответствующей функции
# - осуществление выхода из программы'''



def input_surname():
    return input('Введите фамилию: ').title()

def input_name():
    return input('Введите имя: ').title()

def input_patronymic():
    return input('Введите отчество: ').title()

def input_phone():
    return input('Введите номер телефона: ')

def input_address():
    return input('Введите адрес (город): ').title()

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic} {phone}\n{address}'

def data_input():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as f:
        f.write(f'{contact}\n\n')

def read_file():
    with open('phonebook.txt', 'r', encoding='utf-8') as f:
     return f.read()

def print_data():
    print(read_file())


def search_contact():
    print(
    'Варианты поиска:\n'\
    '1 - по фамилии\n'\
    '2 - по имени\n'\
    '3 - по отчеству\n'\
    '4 - по телефону\n'\
    '5 - по адресу(городу)'
    )
    var = input('Выберите необходимый вариант: ')
    while var not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод данных!')
        var = input('Выберите необходимый вариант: ')
        print()
    i_var = int(var) - 1

    find = input('Введите данные для поиска: ').title()
    print()
    contacts = read_file()
    contacts_list = contacts.strip().split('\n\n')
    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n', ' ').split()
        # print(contact_lst)
        if find in contact_lst[i_var]:
         print(contact_str)
    print()

def copy_line():
    
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        lines= file.readlines()
        for n, line in enumerate(lines, start=1):
            print(f'{n:03}:', line)

    line_number= int(input('Введите номер строки: '))
    if line_number< 1 or line_number > len(lines):
        print('Некорректный номер строки')
        line_number= int(input('Введите номер строки: '))
        print()


    
    with open('phonebook2.txt', 'a',encoding='utf-8' ) as file:
        file.write(lines[line_number -1])

    
    print('Копирование выполнено')
    



def interface():
    with open("phonebook.txt", "a", encoding='utf-8'):
        pass
    choice = ''
    while choice != '4':
        print(
            "Варианты действия: \n" \
            "1 - Ввод данных контакта \n" \
            "2 - Вывести данные на экран \n" \
            "3 - Поиск контакта \n" \
            "4 - копировать \n" \
            "5 - удалить контакт \n" \
            "6 - Выход"
            )
        print()
        choice = input("Выберите номер действия: ")
        print()
        while choice not in ('1', '2', '3', '4','5','6','7'):
            print("Некорректный ввод данных!")
            choice = input("Выберите номер действия: ")
            print()
        match choice:
            case '1':
             data_input()
            case '2':
             print_data()
            case '3':
                search_contact()
            case '4':
                copy_line()
                
            case '6':
                print('Всего доброго!')

if __name__ == '__main__':
    interface()
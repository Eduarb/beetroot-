# list1 = ["str", "str2", 4, 5, 6, True]
# tuple = {"str", "str2", 6, 8, False}

# set1 = {1,1,1,1,1,4,6,}

# str2 = "hello"
# print(set1)
#  функция
# len(srt2)
# print(str2)
# Практичні завдання до 4-ї лекції
# Завдання 1: Основи роботи зі списками (list)
# Створіть список з кількох чисел і додайте в нього нове число. Виведіть оновлений список.
# Видаліть елемент зі списку за індексом і виведіть результат.
# Обчисліть суму всіх елементів списку та виведіть її.
# Знайдіть максимальний і мінімальний елемент у списку.

# list1 = [1, 2, 3, 4, 5,]
# list2 = [6, 7, 8, ]
# list_1_2 = list1+list2
# index_to_remove = 3
# removed_element = list_1_2.pop(index_to_remove)
# print(list_1_2)
# print(removed_element)
# max_element = max(list_1_2)
# min_element = min(list_1_2)
# print(max_element)
# print(min_element)

# Завдання 2: Обхід списку за допомогою циклу for

# Створіть список із кількох рядків. Пройдіться по кожному елементу списку за допомогою циклу for і виведіть його на екран.
# Створіть список чисел. За допомогою for знайдіть і виведіть усі парні числа з цього списку.
# Використовуючи список і for, обчисліть середнє значення чисел у списку.
# Створіть список із різними рядками. Використовуючи for, виведіть довжину кожного рядка.

# my_list = ["Hello", "my name is  Eduard", 2, 23]
# for x in my_list:
#     print(x)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# total_sum = 0
# for x in my_list:
#      total_sum += x
# average = total_sum / len(my_list)
# print(average)

#     if x % 2 == 0:
#      print(x)

# my_list = ["Hello", "my name is  Eduard", "crncrc", "jc4nkenekcecn"]
# for x in my_list:
#     print(f"Довжина рядка '{x}':", len(x))


# Завдання 3: Основи роботи з кортежами (tuple)
# Створіть кортеж із кількох чисел. Спробуйте додати нове число до кортежу і поясніть, чому це неможливо.
# Створіть кортеж із кількох рядків і перетворіть його на список. Додайте новий елемент до списку, а потім знову перетворіть на кортеж.
# Створіть кортеж і використайте for, щоб обійти його елементи. Виведіть кожен елемент на екран.
# Напишіть програму, яка обчислить скільки разів певне число з‘являється в кортежі.

# Завдання 4: Основи роботи з множинами (set)
# Створіть множину із кількох чисел. Додайте новий елемент до множини і виведіть результат.
# Видаліть елемент із множини і спробуйте видалити елемент, якого немає в множині.
# Створіть дві множини і знайдіть їх перетин (спільні елементи) та об’єднання.
# Створіть множину з рядків і перевірте, чи певне слово є у множині.


# Завдання 5: Комбіновані операції з циклами та колекціями
# Створіть список чисел, і використовуючи цикл for, додайте кожне число до множини, щоб отримати список без повторів.
# Створіть кортеж із кількох рядків і використовуйте for, щоб створити новий список, який містить лише унікальні рядки.
tuple1 = ("Cat", "Dog", "Fish", "Dog", "Dog")
tuple2 = tuple(set(tuple1))
for tup in tuple2:
    print(tup)
# Напишіть програму, яка створює множину чисел від 1 до 10, а потім за допомогою циклу for видаляє всі парні числа з множини.

# (edited)


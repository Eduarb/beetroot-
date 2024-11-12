

# The Guessing Game.

# # Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. The result should be sent back to the user via a print statement.

 
# import random
# random_num = random.randint(1,10)
# num_usser = int(input("ВВЕДИ ЧИСЛО ОТ 1 ДО 10: "))
# operator = input(" ваше число должно состоять из {random_num} усовных едениц!")


# import random
# random_num = random.randint(1,10)
# num_usser = int(input("ВВЕДИ ЧИСЛО ОТ 1 ДО 10: "))
# if num_usser == random_num:
#     print("Поздравляю")
# elif num_usser < random_num :
#     print("Ваше число мале, згенеріроване чісло ")
# else:
#     print(f"ваше число: {num_usser} не правильно, правильное число: {random_num}, вы проиграли")

# Task 2

# The birthday greeting program.

# Write a program that takes your name as input, and then your age as input and greets you with the following:

# “Hello <name>, on your next birthday you’ll be <age+1> years”   

# name = input("Введите ваше имя: ")
# age = int(input("Введите ваш возраст: "))
# age2 = age + 1
# print(F"Привет {name}, в следующий день рождения тебе исполнится: {age2} лет")



# Task 3

# Words combination

# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.

# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters 

# 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
# Tips: Use random module to get random char from string)\\

import random
random_string = random.randint (0,5)
string = input("Введите строку: ")
lenght = len(string)
result = string [0],[1],[2],[3],[4],[5]
print(f"'{result}'")



# result = text [0]
# result2 = text [2]
# print(f"'{result}' '{result2}' ")

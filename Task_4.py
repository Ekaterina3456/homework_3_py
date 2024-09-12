# Напишите программу, которая генерирует случайный пароль заданной длины,
# состоящий из букв, цифр и специальных символов.
from random import randint, random, Random, choice

password = ''
len_password = randint(5, 16)
alphabet = 'qwertyuiopasdfghjklzxcvbnm'
symbols = '!@#$%^&*()№?<>'

for i in range(len_password):
    num = randint(1, 3)
    if num == 1:
        i = choice(alphabet)
        password += i
    if num == 2:
        i = randint(0, 9)
        password += str(i)
    if num == 3:
        i = choice(symbols)
        password += i

print("ваш случайный пароль", password)
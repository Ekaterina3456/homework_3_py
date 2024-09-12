# Напишите программу, которая принимает два слова и определяет, являются ли
# они анаграммами.
from sys import flags

word_1 = input('введите первое слово ')
word_2 = input('введите второе слово ')
flag =True

for item in set(word_1):
    for value in set(word_2):
        if item in word_2 or value in word_1:
            if item == value and word_1.count(item) != word_2.count(value):
                flag = False
if flag:
    print('ваши слова анаграммы')
else:
    print('ваши слова не анаграммы')

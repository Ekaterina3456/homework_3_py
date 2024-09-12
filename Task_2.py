# Напишите программу, которая принимает список чисел через строку и
# возвращает наибольшее число в этом списке.

numbers = '23 45 67 12 4 34 6'
list_of_number = numbers.split()
max_num = 0

for value in list_of_number:
    num = int(value)
    if num > max_num:
        max_num = num
print(max_num)

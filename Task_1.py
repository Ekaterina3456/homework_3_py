# Дан список повторяющихся элементов. Вернуть список с дублирующимися
# элементами. В результирующем списке не должно быть дубликатов.

data = [3, 4, 6, 3, 2, 4, 6, 3, 2]
new_data = set(data)
print(new_data)

data_new = []
for item in data:
    if item not in data_new:
        data_new.append(item)
print(data_new)
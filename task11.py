#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(lst)):
    lst[i] += 1
print(lst)

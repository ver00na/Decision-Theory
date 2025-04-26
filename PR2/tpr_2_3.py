import pandas as pd
import numpy as np


def valueD(i, j):
    pij = 0
    nij = 0
    if int(arr[i][0]) < int(arr[j][0]):
        pij += 4
    elif int(arr[i][0]) > int(arr[j][0]):
        nij += 4

    if int(arr[i][1]) > int(arr[j][1]):
        pij += 3
    elif int(arr[i][1]) < int(arr[j][1]):
        nij += 3

    if int(arr[i][2]) > int(arr[j][2]):
        pij += 5
    elif int(arr[i][2]) < int(arr[j][2]):
        nij += 5

    if int(arr[i][3]) > int(arr[j][3]):
        pij += 2
    elif int(arr[i][3]) < int(arr[j][3]):
        nij += 2

    if int(arr[i][4]) < int(arr[j][4]):
        pij += 2
    elif int(arr[i][4]) > int(arr[j][4]):
        nij += 2

    if pij == 0 or nij == 0:
        return 0
    else:
        dij = round(pij / nij, 2)
        return (dij)


arr = np.array([[2000, 25, 5.8, 91, 5],
                [700, 26, 8.8, 88, 6],
                [385, 100, 8.2, 81, 4],
                [550, 27, 9.1, 92, 6],
                [2000, 30, 8, 82, 3],
                [435, 76, 8.8, 92, 7],
                [3000, 50, 8.6, 90, 9],
                [1200, 52, 9.2, 92, 3],
                [2000, 25, 7.1, 86, 4],
                [2800, 40, 7.4, 82, 5],
                [4, 3, 5, 2, 2],
                ['min', 'max', 'max', 'max', 'min']])

arr = arr.astype(object)

print("Начальные данные\n", arr)

for i in range(0, 10):
    if int(arr[i][0]) < 750:
        arr[i][0] = 20
    elif int(arr[i][0]) >= 750 and int(arr[i][0]) <= 2000:
        arr[i][0] = 17
    else:
        arr[i][0] = 13

    if int(arr[i][1]) >= 40:
        arr[i][1] = 15
    else:
        arr[i][1] = 12

    if float(arr[i][2]) >= 9:
        arr[i][2] = 20
    elif float(arr[i][2]) >= 6 and float(arr[i][2]) < 9:
        arr[i][2] = 15
    else:
        arr[i][2] = 3

    if int(arr[i][3]) >= 90:
        arr[i][3] = 13
    elif int(arr[i][3]) >= 70 and int(arr[i][3]) < 90:
        arr[i][3] = 10
    else:
        arr[i][3] = 5

    if int(arr[i][4]) <= 6:
        arr[i][4] = 5
    else:
        arr[i][4] = 2

df = pd.DataFrame(arr,
                  columns=["Цена (-)", "Время прохождения в часах (+)", "Отзывы игроков (+)", "Отзывы журналистов (+)",
                           "Сложность (-)"])
df.index = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'Вес', 'Стремление']
print("Таблица оценок проектов по критериям\n", df)

arr1 = np.zeros([10, 11])
arr1 = arr1.astype(object)

for i in range(10):
    arr1[i][i] = "x"
    for j in range(i + 1, 10):
        D = valueD(i, j)
        if D > 1:
            arr1[j][i] = D
        elif D == 1 or D == 0:
            arr1[j][i] = 0.0
            # arr1[i][j] = '-'
        else:
            # arr1[j][i] = '-'
            arr1[i][j] = 1 / D

for i in range(10):
    for j in range(10):
        if i != j:
            if int(arr1[i][j]) > 0:
                arr1[i][10] += 1

# print(arr1)

df2 = pd.DataFrame(arr1, columns=["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "Количество вхождений"],
                   index=["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"])
print(df2)
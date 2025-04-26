import numpy as np
import pandas as pd

arr = np.array([[10.92, 6.52, 5.0, 1.5, 9.0],
                [11.65, 6.50, 5.0, 1, 8.4],
                [10.39, 6.50, 5.0, 1.5, 8.9],
                [10.80, 6.39, 4.0, 1, 8.8],
                [11.97, 6.50, 5.02, 2, 8.9],
                [10.37, 6.50, 5.0, 1.3, 8.9],
                [11.03, 6.50, 5.0, 2, 9.1],
                [11.99, 6.54, 4.23, 1, 8.3],
                [10.99, 6.30, 5.0, 2, 9.0],
                [10.85, 6.39, 5.2, 1.8, 8.13],
                [5, 2, 3, 4, 2],
                ['min', 'max', 'max', 'max', 'min']])

df = pd.DataFrame(arr, columns=['Цена(-)', 'Диагонал(+)', 'Емкость аккумулятора(+)', 'Страхование(+)', 'Толщина(-)'])
df.index = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'Вес', 'Стремление']

print("Таблица оценок проектов по критериям\n", df)


def valueD(i, j):
    pij = 0
    nij = 0
    if arr[i, 0] < arr[j, 0]:
        pij += float(arr[10, 0])
    elif arr[i, 0] == arr[j, 0]:
        pij += 0
        nij += 0
    else:
        nij += float(arr[10, 0])

    if arr[i, 1] > arr[j, 1]:
        pij += float(arr[10, 1])
    elif arr[i, 1] == arr[j, 1]:
        pij += 0
        nij += 0
    else:
        nij += float(arr[10, 1])

    if arr[i, 2] > arr[j, 2]:
        pij += float(arr[10, 2])
    elif arr[i, 2] == arr[j, 2]:
        pij += 0
        nij += 0
    else:
        nij += float(arr[10, 2])

    if arr[i, 3] > arr[j, 3]:
        pij += float(arr[10, 3])
    elif arr[i, 3] == arr[j, 3]:
        pij += 0
        nij += 0
    else:
        nij += float(arr[10, 3])

    if arr[i, 4] < arr[j, 4]:
        pij += float(arr[10, 4])
    elif arr[i, 4] == arr[j, 4]:
        pij += 0
        nij += 0
    else:
        nij += float(arr[10, 4])

    if nij != 0:
        dij = pij / nij
        return round(dij, 2)
    else:
        return float('inf')


arr1 = np.zeros((10, 10))
arr1 = arr1.astype("object")

for i in range(10):
    for j in range(i + 1, 10):
        if valueD(i, j) > 1:
            arr1[i, j] = valueD(i, j)
        elif valueD(i, j) == 1:
            arr1[i, j] = 0.0
        else:
            arr1[j, i] = valueD(j, i)

df_ = pd.DataFrame(arr1, columns=['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10'])
df_.index = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']

print("\n Полная матрица предпочтений проектов, составленная методом Электра")
print(df_)

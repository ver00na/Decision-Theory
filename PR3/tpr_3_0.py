import numpy as np

table_0 = np.array([[1, 1, 5, 9, 7],
                    [1, 1, 5, 9, 7],
                    [1/5, 1/5, 1, 5, 3],
                    [1/9, 1/9, 1/5, 1, 1/3],
                    [1/7, 1/7, 1/3, 3, 1]])

table_1 = np.array([[1, 1/3, 1/3, 1/9, 1/7],
                     [3, 1, 1, 1/7, 1/7],
                     [3, 1, 1, 1/7, 1/5],
                     [9, 7, 7, 1, 3],
                     [7, 5, 5, 1/3, 1]])

table_2 = np.array([[1, 2, 8, 1/2, 1/2],
                     [1/2, 1, 7, 1/3, 1/3],
                     [1/8, 1/7, 1, 1/9, 1/9],
                     [2, 3, 7, 1, 1],
                     [2, 3, 9, 1, 1]])

table_3 = np.array([[1, 3, 9, 1, 4],
                     [1/3, 1, 9, 1/3, 1/3],
                     [1/9, 1/9, 1, 1/9, 1/4],
                     [1, 3, 9, 1, 4],
                     [1/4, 1/3, 4, 1/4, 1]])

table_4 = np.array([[1, 1, 5, 9, 9],
                     [1, 1, 5, 9, 9],
                     [1/5, 1/5, 1, 5, 5],
                     [1/9, 1/9, 1/5, 1, 1],
                     [1/9, 1/9, 1/5, 1, 1]])

table_5 = np.array([[1, 2, 1/7, 1/8, 1/8],
                     [1/2, 1, 1/5, 1/8, 1/9],
                     [7, 9, 1, 1/3, 1/4],
                     [8, 9, 3, 1, 1/2],
                     [8, 9, 4, 2, 1]])

def calculate_V(matrix):
    n = matrix.shape[0]
    V = []
    for i in range(n):
        row = matrix[i]
        product = np.prod(row)
        V_row = product ** (1/n)
        V.append(V_row)
    return V

V0 = calculate_V(table_0)
V1 = calculate_V(table_1)
V2 = calculate_V(table_2)
V3 = calculate_V(table_3)
V4 = calculate_V(table_4)
V5 = calculate_V(table_5)

sum_V0, sum_V1, sum_V2, sum_V3, sum_V4, sum_V5 = [sum(V) for V in [V0, V1, V2, V3, V4, V5]]

W2i = [V / sum_V0 for V in V0]
W1Y = [V / sum_V1 for V in V1]
W2Y = [V / sum_V2 for V in V2]
W3Y = [V / sum_V3 for V in V3]
W4Y = [V / sum_V4 for V in V4]
W5Y = [V / sum_V5 for V in V5]

S0 = np.sum(table_0, axis=0)
S1 = np.sum(table_1, axis=0)
S2 = np.sum(table_2, axis=0)
S3 = np.sum(table_3, axis=0)
S4 = np.sum(table_4, axis=0)
S5 = np.sum(table_5, axis=0)

P0 = [S0[i] * W2i[i] for i in range(len(S0))]
P1 = [S1[i] * W1Y[i] for i in range(len(S1))]
P2 = [S2[i] * W2Y[i] for i in range(len(S2))]
P3 = [S3[i] * W3Y[i] for i in range(len(S3))]
P4 = [S4[i] * W4Y[i] for i in range(len(S4))]
P5 = [S5[i] * W5Y[i] for i in range(len(S5))]

lambda_max0 = P0[0] + P0[1] + P0[2] + P0[3] + P0[4]
lambda_max1 = P1[0] + P1[1] + P1[2] + P1[3] + P1[4]
lambda_max2 = P2[0] + P2[1] + P2[2] + P2[3] + P2[4]
lambda_max3 = P3[0] + P3[1] + P3[2] + P3[3] + P3[4]
lambda_max4 = P4[0] + P4[1] + P4[2] + P4[3] + P4[4]
lambda_max5 = P5[0] + P5[1] + P5[2] + P5[3] + P5[4]

IS0 = (lambda_max0 - 5) / 4
IS1 = (lambda_max1 - 5) / 4
IS2 = (lambda_max2 - 5) / 4
IS3 = (lambda_max3 - 5) / 4
IS4 = (lambda_max4 - 5) / 4
IS5 = (lambda_max5 - 5) / 4

SI = 1.12

OS0 = IS0 / SI
OS1 = IS1 / SI
OS2 = IS2 / SI
OS3 = IS3 / SI
OS4 = IS4 / SI
OS5 = IS5 / SI

W1 = W2i[0] * W1Y[0] + W2i[1] * W2Y[0] + W2i[2] * W3Y[0] + W2i[3] * W4Y[0] + W2i[4] * W5Y[0]
W2 = W2i[0] * W1Y[1] + W2i[1] * W2Y[1] + W2i[2] * W3Y[1] + W2i[3] * W4Y[1] + W2i[4] * W5Y[1]
W3 = W2i[0] * W1Y[2] + W2i[1] * W2Y[2] + W2i[2] * W3Y[2] + W2i[3] * W4Y[2] + W2i[4] * W5Y[2]
W4 = W2i[0] * W1Y[3] + W2i[1] * W2Y[3] + W2i[2] * W3Y[3] + W2i[3] * W4Y[3] + W2i[4] * W5Y[3]
W5 = W2i[0] * W1Y[4] + W2i[1] * W2Y[4] + W2i[2] * W3Y[4] + W2i[3] * W4Y[4] + W2i[4] * W5Y[4]

Ws = [W1, W2, W3, W4, W5]
for i, value in enumerate(Ws, start=1):
    print(f"W{i}:", value)

max_W = max(W1, W2, W3, W4, W5)
print("Самое большое значение W:", max_W)

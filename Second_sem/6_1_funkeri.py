import numpy as np


def multiplication_matrix(n):
    a = np.array([range(1, n + 1)])
    return a.transpose() @ a


def make_board(n):
    a = np.ones((n, n), dtype="uint8")
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 != 0:
                a[i][j] = 0
    return a


def snake(n, m, direction='H'):
    a = np.zeros((n, m), dtype="int16")
    k = 1
    if direction == 'H':
        for i in range(n):
            if i % 2 == 0:
                a[i] = np.array(range(k, k + m, 1))
            else:
                a[i] = np.array(range(k + m - 1, k - 1, -1))
            k += m
    else:
        for i in range(m):
            if i % 2 == 0:
                a[:, i] = np.array(range(k, k + n, 1))
            else:
                a[:, i] = np.array(range(k + n - 1, k - 1, -1))
            k += n
    return a


def rotate(matrix, angle):
    for i in range(angle // 90):
        matrix = np.rot90(matrix, -1)
    return matrix


def stairs(vector):
    ln = vector.size
    a = np.zeros((ln, ln), dtype=int)
    for i in range(ln):
        a[i] = np.roll(vector, i)
    return a


print(stairs(np.arange(5)))

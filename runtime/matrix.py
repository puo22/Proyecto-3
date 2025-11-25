# runtime/matrix.py
from runtime.memory import MEMORY

def mat_add(A, B):
    return [[a + b for a, b in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]

def mat_sub(A, B):
    return [[a - b for a, b in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]

def mat_mul(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        raise Exception("No se puede multiplicar matrices: dimensiones incompatibles")

    result = [[0 for _ in range(colsB)] for _ in range(rowsA)]

    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                result[i][j] += A[i][k] * B[k][j]

    MEMORY.alloc("mat_mul_result", result)
    return result

def transpose(A):
    T = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    MEMORY.alloc("transpose", T)
    return T


def inverse(A):
    import numpy as np
    inv = np.linalg.inv(np.array(A)).tolist()
    MEMORY.alloc("inverse", inv)
    return inv

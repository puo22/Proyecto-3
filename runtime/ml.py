# runtime/ml.py
import math
from runtime.memory import MEMORY

def linear_regression(X, y, lr=0.01, epochs=300):
    n = len(X)
    m = len(X[0])
    w = [0] * m

    for _ in range(epochs):
        pred = [sum(w[j] * X[i][j] for j in range(m)) for i in range(n)]
        grad = [(2/n) * sum((pred[i] - y[i]) * X[i][j] for i in range(n)) for j in range(m)]
        w = [w[j] - lr * grad[j] for j in range(m)]

    MEMORY.alloc("linreg_model", w)
    return w


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def mlp_predict(x, layers):
    a = x
    for W, b in layers:
        z = [sum(W[i][j] * a[j] for j in range(len(a))) + b[i] for i in range(len(b))]
        a = [sigmoid(z_i) for z_i in z]
    return ao



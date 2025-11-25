# runtime/tensor.py
from runtime.memory import MEMORY

def tensor_shape(t):
    if isinstance(t, list):
        if len(t) == 0:
            return (0,)
        return (len(t),) + tensor_shape(t[0])
    return ()

def tensor_add(A, B):
    if isinstance(A, list):
        out = [tensor_add(a, b) for a, b in zip(A, B)]
    else:
        out = A + B

    MEMORY.alloc("tensor_add", out)
    return out

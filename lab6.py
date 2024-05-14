from lab4_graphical_tests import to_big_bin_string, graph
import numpy as np
import matplotlib.pyplot as plt

def DFT(x):
    c = []
    for i in range(len(x)):
        c.append((-1) ** (1 - int(x[i])))
    n = len(c)
    result = []
    for j in range(n // 2):
        a = b = 0
        for k in range(n):
            a += c[k] * np.cos(2 * np.pi * j * k / n)
            b += c[k] * np.sin(2 * np.pi * j * k / n)
        result.append(np.sqrt(a ** 2 + b ** 2))
    plt.plot(result)
    plt.show()

if __name__ == '__main__':
    sequence = to_big_bin_string(graph(256, 1, 2, 3))
    DFT(sequence)

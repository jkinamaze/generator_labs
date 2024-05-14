from lab4_graphical_tests import to_big_bin_string
import matplotlib.pyplot as plt


def test(x):
    number = x[len(x) - 3]
    if x.count(number) > 1:
        i = x.index(number)
        a = [x[i], x[i + 1], x[i + 2]]
        b = [x[len(x) - 3], x[len(x) - 2], x[len(x) - 1]]
        if a == b and i != len(x) - 3:
            return True


def graph(m, x1, x2, x3):
    x = [x1, x2, x3]
    for i in range(3, 1500):
        x_i = (x[i - 1] + x[i - 2] + x[i - 3]) % m
        x.append(x_i)
        # if test(x):
        #     print('Период', len(x) - 3)
        #     x = x[:-3]
        #     x = x + x
        #     break
    return x


def linear_complexity_profile(sequence):
    sequence = to_big_bin_string(sequence)
    Ls = []
    n = len(sequence)
    C, B, T = [0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(n)]
    C[0] = B[0] = 1
    m = -1
    L = 0
    for N in range(n):
        d = 0
        for j in range(L + 1):
            d = d + C[j] * int(sequence[N - j])
        if (d % 2) == 1:
            T = C[:]
            for i in range(n + m - N):
                C[N - m + i] = C[N - m + i] ^ B[i]
            if L <= N / 2:
                L = N + 1 - L
                m = N
                B = T[:]
        Ls.append(L)
    plt.plot(Ls, color="green", markersize=1)
    plt.show()


if __name__ == "__main__":
    generator = graph(256, 1, 2, 3)
    linear_complexity_profile(generator)
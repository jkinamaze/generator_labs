import matplotlib.pyplot as plt

def berlekamp_massey(sequence):
    n = len(sequence)
    sequence = list(sequence)
    C, B, T = [0 for i in range(n)], [0 for i in range(n)], [0 for i in range(n)]
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
    return C, L


def test(x):
    number = x[len(x) - 3]
    if x.count(number) > 1:
        i = x.index(number)
        a = [x[i], x[i + 1], x[i + 2]]
        b = [x[len(x) - 3], x[len(x) - 2], x[len(x) - 1]]
        if a == b and i != len(x) - 3:
            return True
        

def paint(x, y):
    plt.scatter(x, y, s=0.5, edgecolor="green")
    plt.show()


def graph(C, L, sequence):
    sequence = list(sequence)
    sequence = [int(item) for item in sequence]
    m = 2 ** L
    x = []
    for i in range(10000):
        x_i = 0
        for j in range(1, L + 1):
            if C[j] == 1:
                x_i += sequence[j - 1]
        x_i = x_i % 2
        sequence = sequence[1:] +[x_i]
        s = [str(item) for item in sequence]
        x.append(int(''.join(s), 2) % m)
        a = x[1:]
        b = x[:-1]
        if len(x) > 3:
            if test(x):
                print('\nПериод', len(x) - 3)
                break
    paint(a, b)


def enter():
    sequence = input("Введите строку бит: ")
    C, L = berlekamp_massey(sequence)
    print("Минимальная длина =", L)
    print(C)
    print("Минимальное линейное рекуррентное соотношение:")
    result = []
    for i in range(len(C)):
        if C[i] == 1:
            if i == 0:
                polyelement = "C(x) = 1 + "
                result.append(polyelement)
            else:
                polyelement = "x^"+str(i)+" + "
                result.append(polyelement)
    result[len(result) - 1] = result[len(result) - 1][:-3]
    for i in result:
        print(i, end='')
    graph(C, L, sequence)


if __name__ == "__main__":
    enter()
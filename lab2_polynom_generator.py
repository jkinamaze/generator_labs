import matplotlib.pyplot as plt


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


def graph(m, x1, x2, x3):
    x = [x1, x2, x3]
    for i in range(3, 10000):
        x_i = (x[i - 1] + x[i - 2] + x[i - 3]) % m
        x.append(x_i)
        if test(x):
            print('Период', len(x) - 3)
            break
    return x


def enter():
    m = 256
    x1 = 1
    x2 = 2
    x3 = 3
    x = graph(m, x1, x2, x3)
    a, b = x[1:], x[:-1]
    paint(a, b)


if __name__ == "__main__":
    enter()
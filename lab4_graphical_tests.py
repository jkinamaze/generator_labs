import matplotlib.pyplot as plt


def test(x):
    number = x[len(x) - 3]
    if x.count(number) > 1:
        i = x.index(number)
        a = [x[i], x[i + 1], x[i + 2]]
        b = [x[len(x) - 3], x[len(x) - 2], x[len(x) - 1]]
        if a == b and i != len(x) - 3:
            return True
        

def count_x(x):
    x = sorted(x)
    a, b = [], []
    for i in x:
        if i not in a:
            a.append(i)
            b.append(1)
        else:
            index = a.index(i)
            b[index] = b[index] + 1
    return a, b


def to_big_bin_string(x):
    string = ''
    for i in x:
        a = bin(i)[2:]
        string += a
    return string


def to_bin_mas(x):
    mas = []
    for i in x:
        a = bin(i)[2:]
        mas.append(a)
    return mas


def paint(x, y):
    plt.scatter(x, y, s=0.5, edgecolor="green")
    plt.show()


def test1(a, b):
    plt.bar(a, b, color='green', linewidth=2)
    plt.show()
    

def test2(x, number):
    s = to_big_bin_string(x)
    mas = []
    while len(s) >= number:
        a = s[:number]
        s = s[number:]
        mas.append(a)
    a, b = count_x(mas)
    test1(a, b)


def test3(x):
    a, b = [], []
    number = 0
    temp = 0
    period = 2
    for i in range(len(x)):
        if period == 2:
            temp += 1
            period = 3
            continue
        elif period == 3:
            if x[i] == x[i - 1]:
                temp += 1
                continue
            elif x[i] > x[i - 1]:
                period = 1
            else:
                period = 0
        if period:
            if x[i] >= x[i - 1]:
                temp += 1
            else:
                number += 1
                a.append(number)
                b.append(temp)
                temp = 0
                period = 2
        else:
            if x[i] <= x[i - 1]:
                temp += 1
            else:
                number += 1
                a.append(number)
                b.append(temp)
                temp = 0
                period = 2
    test1(a, b)


def test4(x):
    s = to_big_bin_string(x)
    n = len(s)
    a, b, c = [], [], []
    number = 0
    for i in range(n):
        b.append((-1) ** (1 - int(s[i])))
    for j in range(n):
        m = 0
        k = 0
        for i in range(n):
            m += b[i] * b[(i + j) % n]
            k += b[i] * b[i]
        c.append(m / k)
        number += 1
        a.append(number)
    plt.figure(figsize=(10, 10))
    test1(a, c)


def test5(x):
    mas = to_bin_mas(x)
    a, b, c = [], [], []
    number = 0
    for i in mas:
        i = ''.join(reversed(i))
        b_i = 0
        for j in range(len(i)):
            b_i += ((-1) ** int(i[j])) * (2 ** j)
        b.append(b_i)
    n = len(b)
    for j in range(n):
        m = 0
        k = 0
        for i in range(n):
            m += b[i] * b[(i + j) % n]
            k += b[i] * b[i]
        c.append(m / k)
        number += 1
        a.append(number)
    plt.figure(figsize=(10, 10))
    test1(a, c)



def graph(m, x1, x2, x3):
    x = [x1, x2, x3]
    for i in range(3, 1000):
        x_i = (x[i - 1] + x[i - 2] + x[i - 3]) % m
        x.append(x_i)
        if test(x):
            print('Период', len(x) - 3)
            x = x[:-3]
            break
    return x


def enter():
    m = 256
    x1 = 1
    x2 = 2
    x3 = 3
    x = graph(m, x1, x2, x3)
    while True:
        choice = int(input('Выберите тест:\n'
                        '1. Тест с использованием гистограммы\n'
                        '2. Графический тест\n'
                        '3. Тест проверки на монотонность\n'
                        '4. Тест битовой автокорреляционной функции\n'
                        '5. Тест символьной автокорреляцонной функции\n'
                        '6. Выйти\n'))
        if choice == 1:
            a, b = count_x(x)
            test1(a, b)
        elif choice == 2:
            number = int(input('Введите разрядность числа:\n'))
            test2(x, number)
        elif choice == 3:
            test3(x)
        elif choice == 4:
            test4(x)
        elif choice == 5:
            test5(x)
        else:
            exit()


if __name__ == "__main__":
    enter()
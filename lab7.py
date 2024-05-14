def test1(binx):
    n = len(binx)
    m = 3
    all_count = [0 for _ in range(pow(2, m))]
    t = 0
    while t < n:
        if len(bin_x[t:t + m]) == m:
            all_count[int(bin_x[t:t + m], 2)] += 1
        t += m
    c = (n // m) / pow(2, m)
    xi = (1 / c) * sum(pow(all_count[i] - c, 2) for i in range(len(all_count)))
    # p_value = mpmath.gammainc((pow(2, m) - 1) / 2, xi / 2, regularized=True)
    # print("p-value:", p_value)
    upper_limit = scipy.stats.chi2.ppf(0.95, (pow(2, m) - 1))
    print("xi:", xi, "upper_limit:", upper_limit, "Result:", xi <= upper_limit)


def to_big_bin_string(x):
    string = ''
    for i in x:
        a = bin(i)[2:]
        string += a
    return string


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
    binx = to_big_bin_string(x)
    while True:
        choice = int(input('Выберите тест:\n'
                        '1. Тест с использованием гистограммы\n'
                        '2. Графический тест\n'
                        '3. Тест проверки на монотонность\n'
                        '4. Тест битовой автокорреляционной функции\n'
                        '5. Тест символьной автокорреляцонной функции\n'
                        '6. Выйти\n'))
        if choice == 1:
            test1(binx)
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
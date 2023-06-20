

def fatorial(num, show):
    """

    :param num: número para calcular fatorial
    :param show: aparecer a conta ou não
    :return: fatorial de num
    """
    fact = 1
    if show is True:
        for c in range(num, 0, -1):
            fact *= c
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        return fact

    else:
        for c in range(num, 1, -1):
            fact *= c
        return fact


print(fatorial(5, True))
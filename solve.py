def solve(n, repeats):
    list_ = []
    for i in range(1, repeats + 1):
        list_.append(str(n) * i)
    return sum([int(i) for i in list_])


import math
size = 10**9
x = [True for i in range(size)]
primes = []


def pregenerate():
    global x
    x[0] = x[1] = False
    for i in range(2, size):
        if x[i]:
            primes.append(i)
            for j in range(i*i, size, i):
                x[j] = False


def decomposition(n_: int) -> dict:
    global primes
    d = {}
    if n_ == 1:
        return d
    i = 0
    while n_ != 1:
        if n_ % primes[i] == 0:
            cnt = 0
            while n_ % primes[i] == 0:
                n_ = int(n_ / primes[i])
                cnt += 1
            # print(f'Se divide cu {primes[i]} de {cnt} ori')
            d[primes[i]] = cnt
        i += 1
    return d


def number_of_divisors(d: dict) -> int:
    divs = 1
    for i in d.keys():
        divs *= d[i] + 1
    return divs


if __name__ == "__main__":
    pregenerate()
    # for i in range(40):
    #     if x[i]:
    #         print(f'{i} este prim')
    #     else:
    #         print(f'{i} nu este prim')
    print(f'Pregenerate done')
    for i in range(2, size):
        n = int(i * (i+1) / 2)
        # print(f'n = {n}', end='')
        if n < size and not x[n]:
            t = number_of_divisors(decomposition(n))
            print(f'n = {n}, divisors = {t}')
            if t >= 500:
                break


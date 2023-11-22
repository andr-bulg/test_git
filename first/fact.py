def fact_rec(n):
    if n == 0:
        return 1
    return n * fact_rec(n-1)


if __name__ == '__main__':
    print(fact_rec(5))
    print(fact_rec(0))
    print('Test finished')


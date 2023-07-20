# base case -> zero power
def pow(x, n):
    assert n >= 0 and int(n) == n, 'Not a valid positive integer power'
    if n == 0:
        return 1
    else:
        return x * pow(x, n - 1)
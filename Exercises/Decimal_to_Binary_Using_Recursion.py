def dec_to_bin(n):
    assert n == int(n) and n >= 0, 'Non-negative integers only!'
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * dec_to_bin(int(n / 2))

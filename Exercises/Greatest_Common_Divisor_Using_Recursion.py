def gcd(a, b):
    assert a == int(a) and b == int(b), 'Integers only'
    if a < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
# 1542313
# 1) find remainder by 10 -> 3
# 2) divide by 10 -> 154231
# do 1, 2 until division by 10 results in zero

def sum_of_digits(n):
    assert n >= 0 and int(n) == n, 'Not a valid positive integer'
    total = 0
    while int(n):
        total += n % 10
        n = int(n / 10)
    return total

# by recursion
def sum_of_digits_rec(n):
    assert n >= 0 and int(n) == n, 'Not a valid positive integer'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_of_digits_rec(int(n / 10))
    

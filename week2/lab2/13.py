def is_prime(n):
    if n < 2:
        return False
    m = 2
    while m < n:
        if n % m == 0:
            return False
        m += 1
    return True
n = int(input())
if is_prime(n):
    print("Yes")
else:
    print("No")

    
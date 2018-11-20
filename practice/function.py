def isprime(n):
    if n == 1:
        print("{} is Special".format(n))
        return False
    for x in range(2, n):
        if n % x == 0:
            print("{} equal {} x {}".format(n, x, n // x))
            return False
        else:
            print(n, " is a prime number")
            return True


for n in range(1, 20):
    isprime(n)

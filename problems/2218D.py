import sys, math

testcasenum = int(sys.stdin.readline())
def primes():
    yield (2, 3)
    primes = [2, 3]
    n = 5
    
    while True:
        is_prime = True
        limit = int(n ** 0.5) + 1
        for p in primes:
            if p > limit:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            yield (primes[-1], n)
            primes.append(n)
        n += 2
for _ in range(testcasenum) :
    # arrlen = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    # nums = [int(u) for u in sys.stdin.readline().split()]
    res = []
    for adjprimes in primes() :
        fprime, sprime = adjprimes
        val = fprime * sprime
        res.append(val)
        if len(res) == n : break
    print(" ".join(str(u) for u in res))
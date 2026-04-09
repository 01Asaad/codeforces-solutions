import sys, math

testcasenum = int(sys.stdin.readline())

for _ in range(testcasenum) :
    # arrlen = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    # nums = [int(u) for u in sys.stdin.readline().split()]
    res = []
    s, mid, f = 1, n+1, n+2
    while len(res) != n * 3 :
        res += [s, mid, f]
        s += 1
        mid += 2
        f += 2
    print(" ".join(str(u) for u in res))
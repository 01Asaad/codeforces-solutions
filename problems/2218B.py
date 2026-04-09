import sys, math

testcasenum = int(sys.stdin.readline())

for _ in range(testcasenum) :
    # arrlen = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    # nums = [int(u) for u in sys.stdin.readline().split()]
    res = []
    mid = n+1
    for i in range(1, n+1) :
        res += [i, mid, mid+1]
        mid+=1
    print(" ".join((str(u) for u in res)))

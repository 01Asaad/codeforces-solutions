import sys, math

testcasenum = int(sys.stdin.readline())

for _ in range(testcasenum) :
    # arrlen = int(sys.stdin.readline())
    n, k = [int(u) for u in sys.stdin.readline().split()]
    print(n if k<n-1 else 1)
    
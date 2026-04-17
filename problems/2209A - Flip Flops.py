import sys, math

testcasenum = int(sys.stdin.readline())

for _ in range(testcasenum) :
    n, c, k = (int(u) for u in sys.stdin.readline().split())
    nums = [int(u) for u in sys.stdin.readline().split()]

    nums.sort()
    for monster in nums :
        if monster > c : break
        fftothrow = min(c - monster, k)
        c+=monster + fftothrow
        k-=fftothrow
    print(c)
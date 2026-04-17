import sys, math
testcasenum = int(sys.stdin.readline())

for _ in range(testcasenum) :
    n, m = (int(u) for u in sys.stdin.readline().split())
    nums = (int(u) for u in sys.stdin.readline().split())
    adjdupes = 0
    prevval = None
    for i, num in enumerate(nums) :
        adjdupes = (adjdupes+1) if num==prevval else 1
        prevval = num
        if adjdupes == m :
            print("NO")
            break
    else :
        print("YES")
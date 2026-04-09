import sys, math

testcasenum = int(sys.stdin.readline())

for _ in range(testcasenum) :
    arrlen = int(sys.stdin.readline())
    nums = [int(u) for u in sys.stdin.readline().split()]
    maxres = -float("inf")
    for num in nums :
        for num2 in nums :
            maxres = max(maxres, num ^ num2)
    
    print(maxres)
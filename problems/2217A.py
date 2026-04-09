import sys, math

testcasenum = int(sys.stdin.readline())

for _ in range(testcasenum) :
    arrlen, k = (int(u) for u in sys.stdin.readline().split())
    nums = [int(u) for u in sys.stdin.readline().split()]
    print("NO" if (arrlen % 2 != 0 and sum(nums) %2 ==0) and k%2 != 0 else "YES")
import sys, math

# testcasenum = int(sys.stdin.readline())
testcasenum = 1
for _ in range(testcasenum) :
    arrlen = int(sys.stdin.readline())
    nums = [int(u) for u in sys.stdin.readline().split()]
    for i, plane in enumerate(nums) :
        if nums[nums[plane - 1] - 1] == i+1 :
            print("YES")
            break
    else :
        print("NO")

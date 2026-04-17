import sys, math

testcasenum = int(sys.stdin.readline())

for _ in range(testcasenum) :
    arrlen = int(sys.stdin.readline())
    nums = [int(u) for u in sys.stdin.readline().split()]
    nums.sort(reverse=True)
    for i, num in enumerate(nums) :
        if num == nums[i-1] and arrlen > 1 :
            print("-1")
            break
    else :
        print(" ".join(str(u) for u in nums))
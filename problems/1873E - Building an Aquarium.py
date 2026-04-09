import sys, math

testcasenum = int(sys.stdin.readline())

for _ in range(testcasenum) :
    arrlen, maxw = (int(u) for u in sys.stdin.readline().split())
    nums = [int(u) for u in sys.stdin.readline().split()]
    nums.sort()
    subtract= []
    subtract.append(nums[0])
    for i in range(1, arrlen) :
        subtract.append(nums[i] + subtract[-1])
    h = 0
    w = 0
    for i in range(arrlen) :
        h=nums[i]
        w = ((i +1) * h) - subtract[i]
        if w > maxw :
            w = ((i) * nums[i-1]) - subtract[i-1]
            h=nums[i-1] + (maxw - w)//(i) + 1
            break
    else :
        h=(maxw - w) // arrlen + h + 1
    print(h -1)
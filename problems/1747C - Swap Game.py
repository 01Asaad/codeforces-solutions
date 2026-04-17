import sys, math

testcasenum = int(sys.stdin.readline())

for _ in range(testcasenum) :
    arrlen = int(sys.stdin.readline())
    nums = [int(u) for u in sys.stdin.readline().split()]
    mini = min((nums[i] for i in range(1, len(nums))))
    print("ALICE" if mini < nums[0] else "BOB")
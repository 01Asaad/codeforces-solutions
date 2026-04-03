import sys

length = int(sys.stdin.readline())
nums = [int(u) for u in sys.stdin.readline().split()]
max = 0
for i, num in enumerate(nums) :
    if num > nums[max] :
        max = i
for i in range(max + 1, len(nums)) :
    if nums[i] > nums[i-1] : print("no");exit()
for i in range(max - 1, -1, -1) :
    if nums[i] > nums[i+1] : print("no");exit()
print("yes")
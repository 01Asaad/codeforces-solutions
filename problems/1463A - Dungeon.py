import sys, math

testcasenum = int(sys.stdin.readline())

for _ in range(testcasenum) :
    # arrlen = int(sys.stdin.readline())
    monsters = [int(u) for u in sys.stdin.readline().split()]
    summ = sum(monsters)
    print("YES" if summ % 9 == 0 and all((monster >= (summ//9)) for monster in monsters) else "NO")
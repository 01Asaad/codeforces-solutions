import sys, math

n, m, a = [int(u) for u in sys.stdin.readline().split()]
print(math.ceil(n/a)*math.ceil(m/a))
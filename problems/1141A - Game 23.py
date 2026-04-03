import sys


n, m = (int(u) for u in sys.stdin.readline().split())
factors = {2: 0, 3: 0}
diff = m / n
if not diff.is_integer() : print(-1);exit()
diff = int(diff)

while diff % 2 == 0:
    factors[2] += 1
    diff //= 2
d = 3
while d * d <= diff:
    while diff % d == 0:
        if d != 2 and d!=3 : print(-1);exit()
        factors[d] +=1
        diff //= d
    d += 2
if diff > 1:
    if diff != 3 : print(-1);exit()
    factors[3] +=1
print(sum(factors.values()))

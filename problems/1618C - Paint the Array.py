import math
import sys

n = int(sys.stdin.readline())

for _ in range(n) :
    arrlen = int(sys.stdin.readline())
    arr = [int(u) for u in sys.stdin.readline().split()]
    gcd_of_first, gcd_of_second = None, None
    for i, num in enumerate(arr) :
        if i % 2 == 0 :
            gcd_of_first = math.gcd(gcd_of_first, num) if gcd_of_first is not None else num            
        else :
            gcd_of_second = math.gcd(gcd_of_second, num) if gcd_of_second is not None else num
    if gcd_of_first is None :
        print(gcd_of_second)
        continue
    elif gcd_of_second is None :
        print(gcd_of_first)
        continue
    for i in range(0, arrlen, 2) :
        num = arr[i]
        if num % gcd_of_second == 0 :
            break
    else :
        print(gcd_of_second)
        continue
    for i in range(1, arrlen, 2) :
        num = arr[i]
        if num % gcd_of_first == 0 :
            found = False
            break
    else :
        print(gcd_of_first)
        continue
    print(0)
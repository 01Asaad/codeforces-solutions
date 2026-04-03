import math
import sys


num = int(sys.stdin.readline())
for _ in range(num) :
    n, r, b = (int(u) for u in sys.stdin.readline().split())
    res = ""
    di = math.floor(r/(b+ 1))
    mod = r % (b+1)
    mods_placed = 0
    bs = 0
    for i in range(r - mod) :
        if (i+1) % di == 0 and bs < b:
            bs+=1
            if mods_placed != mod :
                res+="R"
                mods_placed+=1
            res+="RB"
        else : res+= "R"
    print(res)
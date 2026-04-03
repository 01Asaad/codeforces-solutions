import sys

length = sys.stdin.readline()
for _ in range(int(length)) :
    n, m = [int(u) for u in sys.stdin.readline().split()]
    nums = (int(u) for u in sys.stdin.readline().split())
    mods = [0] * m
    lists_len = 0
    for i in nums :
        realmod = (i % m)
        mod = m - (realmod if realmod else m)
        mods[mod] += 1
    if mods[0] :
        lists_len +=1
    for i, mod in enumerate(mods[1:len(mods) // 2 + 1], 1) :
        val_of_rem_of_mod = mods[len(mods) - i]
        diff = abs(mod - val_of_rem_of_mod)
        if not diff and mod > 0 : lists_len +=1
        else :
            lists_len +=diff
    print(lists_len)

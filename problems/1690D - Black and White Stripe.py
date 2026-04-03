import sys
 
# import cProfile
# import pstats
# profiler = cProfile.Profile()
# profiler.enable()
 
num = int(sys.stdin.readline())
for _ in range(num) :
    length, k = (int(o) for o in sys.stdin.readline().split())
    stripes = sys.stdin.readline()
    whites = 0
    for i in range(k) :
        if stripes[i] == "W" : whites +=1
    minimum_whites = whites
    start, end = 0, k - 1
    for i in range(k, length) :
        # to_be_removed = stripes[start]
        # to_be_added = stripes[i]
        end +=1
        if stripes[start] == stripes[i] : pass
        elif stripes[start] == "W" : whites -= 1
        else : whites += 1
        start +=1
        minimum_whites = min(minimum_whites, whites)
 
    print(minimum_whites)
# profiler.disable()
# stats = pstats.Stats(profiler)
# stats.sort_stats('cumulative')
# stats.print_stats(10)
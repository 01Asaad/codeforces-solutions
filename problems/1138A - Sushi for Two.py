import sys
 
# import cProfile
# import pstats
# profiler = cProfile.Profile()
# profiler.enable()
 
num = int(sys.stdin.readline())
# for _ in range(num) :
    # length = int(sys.stdin.readline())
word = sys.stdin.readline().split()
max_diff = 2
curr = word[0]
precons = 1
postconsaim = None
postcons = 1
for i in range(1, len(word)) :
    char = word[i]
    if curr == char :
        precons += 1
        postcons += 1
        if postcons*2 > max_diff and postconsaim and postcons <= postconsaim :
            max_diff = max(max_diff, postcons * 2)
        if postcons == postconsaim : postconsaim = None
    else :
        curr = char
        postconsaim = precons
        postcons = 1
        precons = 1
print(max_diff)
 
# profiler.disable()
# stats = pstats.Stats(profiler)
# stats.sort_stats('cumulative')
# stats.print_stats(10)
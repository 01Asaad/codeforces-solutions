import sys

num  = int(sys.stdin.readline())
gifts = [int(u) for u in sys.stdin.readline().split()]

gifts.sort()
sorted = gifts
mid = num // 2
small = sorted[:mid]
big = sorted[mid:]
done = []
donenum = mid -1
for i in range(num//2) :
    done.append(big[i])
    done.append(small[i])
if len(big) == num//2 +1 :
    donenum +=1
    done.append(big[num//2])
print(donenum)
print(" ".join((str(i) for i in done)))
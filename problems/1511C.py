import sys, math
from typing import Optional

# testcasenum = int(sys.stdin.readline())
class Node :
    def __init__(self, val, next= None) -> None:
        self.val = val
        self.next = next

# for _ in range(testcasenum) :
decklen, querieslen = (int(u) for u in sys.stdin.readline().split())
deck = [int(u) for u in sys.stdin.readline().split()]
queries = [int(u) for u in sys.stdin.readline().split()]
root = Node(deck[0])
last = root
for i in range(1, decklen) :
    pp = Node(deck[i])
    last.next = pp
    last = pp
res = []
for query in queries :
    # print(deck)
    current = root
    count = 0
    prev = None
    while True :
        if current.val == query :
            res.append(count +1)
            if count :
                prev.next = current.next
                current.next = root
            root = current
            break
        prev = current
        current = current.next
        count+=1
print(" ".join(str(u) for u in res))
import sys

num  = int(sys.stdin.readline())
gifts = [int(u) for u in sys.stdin.readline().split()]

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    return arr


sorted = list(heap_sort(gifts))
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
import sys
 
 
num = int(sys.stdin.readline())
# for _ in range(num) :
 
cols = [int(i) for i in sys.stdin.read().split()]
def calc(cols, col_index) :
    if col_index == 0 : return
    col, prevcol = cols[col_index], cols[col_index - 1]
    if col < prevcol :
        diff = prevcol - col
        cols[col_index - 1] -= diff
        cols[col_index] += diff
        calc(cols, col_index - 1)
for i in range(1, len(cols)) :
    calc(cols, i)
print(" ".join((str(i) for i in cols)))
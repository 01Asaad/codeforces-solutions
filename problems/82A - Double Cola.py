import math
import sys

n = int(sys.stdin.readline())

def end_of_loop(n, olval = None) :
    if n == -1 : return 0
    return 5*(2**n) + (olval if olval is not None else end_of_loop(n - 1))
def length(n) :
    return 5*math.pow(2, n)
def closed_form_series(n) :
    return 5*(2**(n+1)) - 5
CHARS = ("Sheldon", "Leonard", "Penny", "Rajesh", "Howard")

pp = 0
olval = 0
while True :
    # val = closed_form_series(pp)
    val = end_of_loop(pp, olval)
    if val >= n :
        break
    olval = val
    pp +=1
start = olval + 1
l = length(pp)
offset = n - start
split = l / 5
char = CHARS[math.floor(offset / split)]
print(char)
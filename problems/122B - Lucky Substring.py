import sys
digits = sys.stdin.readline()
sevens = 0
fours = 0
for digit in digits :
    if digit == "7" :sevens +=1
    elif digit == "4" : fours +=1
if not sevens and not fours : print("-1")
elif fours >= sevens : print("4")
else : print("7")

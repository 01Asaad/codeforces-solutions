import sys
 
 
num = int(sys.stdin.readline())
LETTERS = "abcdefghijklmnopqrstuvwxyz"
for _ in range(num) :
    length = int(sys.stdin.readline())
    word = sys.stdin.readline().strip().split()
    used_letters = []
    used_letters_count = []
    sol = ""
    for char in word :
        char = int(char)
        if int(char) == 0 :
            for letter in LETTERS :
                if letter not in used_letters :
                    used_letters.append(letter)
                    used_letters_count.append(1)
                    break
        else :
            i = used_letters_count.index(char)
            letter = used_letters[i]
            used_letters_count[i] += 1
        sol += letter
    print(sol)
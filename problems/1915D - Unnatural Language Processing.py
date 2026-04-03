import sys
 
 
num = int(sys.stdin.readline())
for _ in range(num) :
    length = int(sys.stdin.readline())
    word = sys.stdin.readline().strip()
    splitted = []
    syllable = ""
    for i, char in enumerate(word) :
        if char in ["d", "b", "c"] :
            if i == len(word) - 1 :
                syllable += char
                splitted.append(syllable)
                syllable = ""
            elif i and word[i - 1] in ["d", "b", "c"] :
                splitted[-1] += syllable
                syllable = char
            elif i and word[i - 1] in ["a", "e"] :
                splitted.append(syllable)
                syllable = char
            else :
              syllable += char  
        else :syllable += char
    if syllable :
        splitted.append(syllable)
    print(".".join(splitted))
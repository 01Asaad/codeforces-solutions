import random

def generate_nums_input(length = 1000000, min = 0, max = 1000000) :
    return random.choices(range(min, max), k=length)
def generate_unique_nums_input(length = 100000, min = 0, max = 1000000) :
    return random.sample(range(min, max), k=length)

if __name__ == "__main__" :
    print(" ".join(str(I) for I in generate_nums_input(100, 1, 1000000000000000000))) #(pipe stdout to file)
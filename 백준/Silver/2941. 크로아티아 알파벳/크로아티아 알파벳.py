import sys
input = sys.stdin.readline
print = sys.stdout.write

word_list = list(input().rstrip())
max_idx = len(word_list)

for x in range(1 , len(word_list)):
    if (word_list[x] == "-"):
        max_idx -= 1
    
    if (word_list[x] == "j"):
        if word_list[x - 1] == "l" or word_list[x - 1] == "n":
            max_idx -= 1
    
    if (word_list[x] == "="):
        if (x > 1 and word_list[x - 1] == "z" and word_list[x - 2] == "d"):
            max_idx -= 2
        else: 
            max_idx -= 1
print(str(max_idx))
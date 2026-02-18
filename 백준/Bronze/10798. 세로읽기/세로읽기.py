import sys
input = sys.stdin.readline
print = sys.stdout.write

arr = []
max_idx = 0

for _ in range(5):
    word = input().rstrip()
    max_idx = max(max_idx , len(word))
    arr.append(word)

split_box = [["+"] * max_idx for _ in range(5)]
for i in range(5):
    for j in range(len(arr[i])):
        split_box[i][j] = arr[i][j:j + 1:1]

for i in range(max_idx):
    for j in range(5):
        if (split_box[j][i] != "+"): print(str(split_box[j][i]))
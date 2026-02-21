import sys
input = sys.stdin.readline
print = sys.stdout.write

length = list(map(int , input().rstrip().split()))
length.sort()

if length[2] >= length[1] + length[0]:
    print(str((length[0] + length[1]) * 2 - 1))
else: print(str(length[0] + length[1] + length[2]))
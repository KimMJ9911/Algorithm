import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())
arr = list(map(int , input().rstrip().split()))
max_val = max(arr)
ans = 0

for x in range(n):
    arr[x] = (arr[x] / max_val) * 100

print(str(sum(arr) / n))

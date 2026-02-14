import sys
input = sys.stdin.readline
print = sys.stdout.write

n , m = map(int , input().rstrip().split())
arr = list(map(int , input().rstrip().split()))
ans = []

for x in range(n):
    if (arr[x] < m): 
        ans.append(arr[x])

print(" ".join(map(str , ans)))
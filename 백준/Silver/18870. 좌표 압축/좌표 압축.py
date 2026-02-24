import sys
input = sys.stdin.readline
print = sys.stdout.write

s = set()
n = int(input().rstrip())
arr = list(map(int , input().rstrip().split()))
sorted_arr = sorted(list(set(arr)))

rank = {val : idx for idx , val in enumerate(sorted_arr)}
ans = []
for x in arr:
    ans.append(rank[x])

print(" ".join(map(str , ans)))
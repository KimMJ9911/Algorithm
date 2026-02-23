import sys
from itertools import combinations
input = sys.stdin.readline
print = sys.stdout.write

n , m = map(int , input().rstrip().split())
cards = list(map(int , input().rstrip().split()))
ans = float('-inf')

for x in combinations(cards , 3):
    s = sum(x)
    if s <= m:
        ans = max(s , ans)

print(str(ans))
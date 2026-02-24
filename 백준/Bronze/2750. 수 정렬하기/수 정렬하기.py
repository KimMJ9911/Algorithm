import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())
arr = []
for _ in range(n):
    arr.append(int(input().rstrip()))
arr.sort()
print("\n".join(map(str , arr)))
import sys
input = sys.stdin.readline
print = sys.stdout.write

n , m = map(int , input().rstrip().split())
arr = list(range(1 , n + 1))

for _ in range(m):
    start , end = map(int , input().rstrip().split())
    left = start - 1
    right = end - 1

    while left < right:
        arr[left] , arr[right] = arr[right] , arr[left]
        left += 1
        right -= 1

print(" ".join(map(str , arr)))
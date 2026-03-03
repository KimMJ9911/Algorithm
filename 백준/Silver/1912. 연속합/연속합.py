import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())
arr = list(map(int , input().rstrip().split()))
dp = [0] * n
dp[0] = arr[0]

for i in range(1 , n):
    dp[i] = max(dp[i - 1] + arr[i] , arr[i])

ans = max(dp)
print(str(ans))
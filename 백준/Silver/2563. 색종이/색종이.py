import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
board = [[0] * 101 for _ in range(101)]

for _ in range(n):
    degree = list(map(int , input().split()))
    for i in range(degree[0] , degree[0] + 10):
        for j in range(degree[1] , degree[1] + 10):
            board[i][j] = 1

cnt = 0

for i in range(1 , 101):
    for j in range(1 , 101):
        if (board[i][j] == 1): cnt += 1
print(str(cnt))
import sys
input = sys.stdin.readline
print = sys.stdout.write

chess_board = [1 , 1 , 2 , 2 , 2 , 8]
piece = list(map(int , input().rstrip().split()))
ans = []

for i in range(6):
    ans.append(chess_board[i] - piece[i])

print(" ".join(map(str , ans)))
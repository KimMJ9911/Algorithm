import sys
input = sys.stdin.readline
print = sys.stdout.write

sudoku = [list(map(int , input().rstrip().split())) for _ in range(9)]
zeros = [(i , j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def check(x , y , val):
    for i in range(9):
        if sudoku[x][i] == val or sudoku[i][y] == val:
            return False
    div_x = (x // 3) * 3
    div_y = (y // 3) * 3
    for i in range(div_x , div_x + 3):
        for j in range(div_y , div_y + 3):
            if sudoku[i][j] == val:
                return False
    return True

def dfs(depth):
    if depth == len(zeros):
        for row in sudoku:
            print(" ".join(map(str , row)) + "\n")
        sys.exit()
    x , y = zeros[depth]
    for i in range(1 , 10):
        if check(x , y , i):
            sudoku[x][y] = i
            dfs(depth + 1)
            sudoku[x][y] = 0

dfs(0)
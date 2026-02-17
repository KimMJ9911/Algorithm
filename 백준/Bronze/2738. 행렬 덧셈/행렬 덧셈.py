import sys
input = sys.stdin.readline
print = sys.stdout.write

n , m = map(int , input().rstrip().split())
arr_1 = [[0] * m for _ in range(n)]
arr_2 = [[0] * m for _ in range(n)]

for i in range(n):
    arr_1[i] = list(map(int , input().rstrip().split()))

for i in range(n):
    arr_2[i] = list(map(int , input().rstrip().split()))

for i in range(n):
    for j in range(m):
        print(str(arr_1[i][j] + arr_2[i][j]) + " ")
    print("\n")
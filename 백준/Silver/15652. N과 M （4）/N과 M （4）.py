import sys
input = sys.stdin.readline
print = sys.stdout.write

def DFS(k):
    if len(arr) == m:
        print(" ".join(map(str , arr)) + "\n")
        return

    for i in range(k , n):
        arr.append(i + 1)
        DFS(i)
        arr.pop()

n , m = map(int , input().rstrip().split())
arr = []

DFS(0)
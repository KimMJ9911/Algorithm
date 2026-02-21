import sys
input = sys.stdin.readline
print = sys.stdout.write

def BFS(depth):
    if depth == m:
        print(" ".join(map(str , arr)) + "\n")
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr[depth] = i + 1
            BFS(depth + 1)
            arr[depth] = 0
            visited[i] = False

n , m = map(int , input().rstrip().split())
visited = [False for _ in range(n)]
arr = [0 for _ in range(m)]

BFS(0)
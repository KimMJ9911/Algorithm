import sys
input = sys.stdin.readline
print = sys.stdout.write

x , y , w , h = map(int , input().rstrip().split())
print(str(min(w - x , h - y , x , y)))
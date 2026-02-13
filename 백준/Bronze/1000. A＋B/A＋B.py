import sys
input = sys.stdin.readline
print = sys.stdout.write

a,b = map(int , input().split())
ans = a + b
print(str(ans).rstrip())
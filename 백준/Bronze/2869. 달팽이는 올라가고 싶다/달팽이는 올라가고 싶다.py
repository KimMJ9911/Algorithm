import sys
input = sys.stdin.readline
print = sys.stdout.write

a , b , v = map(int , input().rstrip().split())

cnt = 1
climb = v - a
up = a - b

if climb > 0:
    if climb % up > 0:
        cnt += climb // up + 1
    else: cnt += climb // up

print(str(cnt))
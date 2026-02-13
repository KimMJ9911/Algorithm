import sys
put = sys.stdin.readline
print = sys.stdout.write

n = int(put().rstrip())
for i in range(n):
    a , b = map(int , put().rstrip().split())
    print(str(a + b) + "\n")
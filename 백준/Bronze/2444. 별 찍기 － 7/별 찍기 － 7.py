import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())
for i in range(1 , n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1) + "\n")

for i in range (n - 1 , 0 , -1):
    print(" " * (n - i) + "*" * (2 * i - 1) + "\n")
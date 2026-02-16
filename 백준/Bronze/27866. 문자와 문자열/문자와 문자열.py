import sys
input = sys.stdin.readline
print = sys.stdout.write

word = input().rstrip()
n = int(input().rstrip())

print(word[n - 1:n:])
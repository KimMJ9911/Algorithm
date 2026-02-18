import sys
input = sys.stdin.readline
print = sys.stdout.write

word , n = input().rstrip().split()
init = int(n)
code = [ord(x) - ord('A') + 10 if x >= 'A' else int(x) for x in word]
ans = 0

for i in code:
    ans += i
    ans *= init

print(str(ans // init))
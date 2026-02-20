import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())
div = 2
ans = []
while n != 1:
    if n % div == 0:
        ans.append(div)
        n //= div
    else: div += 1

print("\n".join(map(str , ans)))
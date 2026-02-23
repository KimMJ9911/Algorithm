import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())
ans = 0

idx_5 = n // 5
avalible = False
for i in range(idx_5 , -1 , -1):
    val = n
    ans = 0
    val -= 5 * i
    if (val % 3 == 0): 
        ans += val // 3 + i
        avalible = True
        break
if not avalible: print(str(-1))
else: print(str(ans))
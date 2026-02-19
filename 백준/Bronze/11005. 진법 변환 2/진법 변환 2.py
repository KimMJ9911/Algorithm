import sys
input = sys.stdin.readline
print = sys.stdout.write

n , b = map(int , input().rstrip().split())
ans = []
while n > 0:
    if n % b > 9:
        ans.append(chr(n % b + ord('A') - 10))
    else:
        ans.append(n % b)
    n //= b

ans.reverse()
print("".join(map(str , ans)))
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = input().rstrip()

num = int(n)
idx = len(n)
exist = False

if num < 19:
    for x in range(1 , num):
        s = list(map(int , str(x)))
        ans = sum(s) + x
        if ans == num:
            print(str(x))
            exist = True
            break
else:
    for x in range(num - 9 * idx , num):
        s = list(map(int , str(x)))
        ans = sum(s) + x
        if ans == num:
            print(str(x))
            exist = True
            break

if not exist: print(str(0))
import sys
input = sys.stdin.readline
print = sys.stdout.write

init = list(map(int , input().rstrip().split()))
package = []
one = []
cnt = init[0]
cost = 0

for _ in range(init[1]):
    n , m = map(int , input().rstrip().split())
    package.append(n)
    one.append(m)

package.sort()
one.sort()

min_package = package[0]
min_one = one[0]

while cnt > 0:
    if cnt < 6:
        if min_package <= min_one * cnt:
            cost += min_package
        else:
            cost += min_one * cnt
    else:
        if (min_package <= min_one * 6):
            cost += min_package
        else:
            cost += min_one * 6
    cnt -= 6

print(str(cost))
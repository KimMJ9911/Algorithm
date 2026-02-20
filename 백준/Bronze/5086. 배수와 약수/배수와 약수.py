import sys
input = sys.stdin.readline
print = sys.stdout.write

while True:
    n , m = map(int , input().rstrip().split())
    if n == 0 and m == 0: break

    if (n != 0 and m != 0):
        if n % m == 0: print("multiple")
        elif m % n == 0: print("factor")
        else: print("neither")
    print("\n")
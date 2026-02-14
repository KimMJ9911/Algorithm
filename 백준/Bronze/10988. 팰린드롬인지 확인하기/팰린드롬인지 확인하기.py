import sys
input = sys.stdin.readline
print = sys.stdout.write

word = input().rstrip()
reversed_word = word[::-1]

if (word == reversed_word):
    print(str(1))
else: print(str(0))
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())
user_data = []
for _ in range(n):
    age , name = map(str , input().rstrip().split())
    user_data.append((int(age) , name))
ans = sorted(user_data , key = lambda x : x[0])

for key , value in ans:
    print(f"{key} {value}" + "\n")
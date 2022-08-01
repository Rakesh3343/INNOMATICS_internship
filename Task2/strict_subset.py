A = set(input().split())
N = int(input())
output = True

for i in range(N):
    s = set(input().split())
    if not s.issubset(A):
        output = False
    if len(s) >= len(A):
        output = False

print(output)
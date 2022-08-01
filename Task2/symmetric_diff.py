m = input()
a = list(map(int, input().split()))
n = input()
b = list(map(int, input().split()))
a = set(a) ; b = set(b)
c = a^b
for i in sorted(c):
    print(i)
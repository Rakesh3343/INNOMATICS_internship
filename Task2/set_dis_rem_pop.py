n=int(input())
s=set(map(int,input().split()))
N=int(input())
for i in range(N):
    choice=input().split()
    if choice[0] == 'pop':
        s.pop()
    if choice[0] == 'remove':
        if int(choice[1]) in s:
            s.remove(int(choice[1]))
    if choice[0] == 'discard':
        if int(choice[1]) in s:
            s.discard(int(choice[1]))

print(sum(s))

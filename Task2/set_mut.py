n = int(input())
A = set(map(int, input().split()))
N = int(input())

for i in range(N):
    choice = (input().split())
    a = set(map(int, input().split()))
    if choice[0]=='intersection_update':
        A.intersection_update(a)
    elif choice[0] == 'update':
        A.update(a)  
    elif choice[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(a)
    elif choice[0] == 'difference_update':
        A.difference_update(a)          
print(sum(A))

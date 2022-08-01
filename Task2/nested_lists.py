l=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    l.append([name,score])
l.sort(key=lambda x:x[1])
s=[]
for i in l:
    s.append(i[1])
second=[]
for i in l:
    if (i[1]==(sorted(list(set(s)))[1])):
        second.append(i[0])
for i in sorted(second):
    print(i)
n=int(input())
nxt = n
while True:
    fc=0
    for i in range(1,nxt+1):
        if nxt % i == 0:
            fc+=1
    if fc==2:
        break
    nxt+=1
    
pre = n    
while True:
    fc=0
    for i in range(1,pre+1):
        if pre % i == 0:
            fc+=1
    if fc==2:
        break
    pre-=1

if n-pre <= nxt-n:
    print(n-pre)
else:
    print(nxt-n)
    
            
t=int(input())
for _ in range(t):
    n=int(input())
    np=n
    while True:
        fc=0
        for i in range(1,np+1):
            if np%i==0:
                fc+=1
        if fc==2:
            break
        np+=1
        
    pp=n
    while True:
        fc=0
        for i in range(1,pp+1):
            if pp%i==0:
                fc+=1
        if fc==2:
            break
        pp-=1
    
    if n-pp <= np-n:
        print(pp)
    else:
        print(np)
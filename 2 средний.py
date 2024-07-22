def vsed(n):
    a = []
    if n**0.5==int(n**0.5):
        for d in range(2, int(n**0.5)):
            if n%d==0:
                a.append(d)
                a.append(n//d)
    if len(a)==2:
        return a[0]
    else:
        return 0

for i in range(400000,2000000+1):
    s = vsed(i)
    if s!=0:
        print(i, s)
    
            

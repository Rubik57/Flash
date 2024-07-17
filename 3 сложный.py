def prime(n):
    for d in range(2, int(n**0.5)+1):
        if n %d ==0:
            return False
    return True

def prd(n):
    vsed = []
    for d in range(2, int(n**0.5)+1):
        if n%d==0:
            if prime(d):
                vsed.append(d)
            if prime(n//d) and d*d!=n:
                vsed.append(n//d)
    if len(vsed)>2:
        return vsed
    else:
         return 0

k = 0
for i in range(100001, 10**10):
    s = prd(i)
    if s!=0 and sum(s)%171==0 and i%100==23:
        print(i, len(s))
        k+=1
        if k==5:
            break

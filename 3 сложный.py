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
def sc(n):
    res = 0
    while n>0:
        res += n%10
        n//=10
    return res

maxs = 0
k = 0
for i in range(100001, 10**10):
    s = prd(i)
    if s!=0 and sum(s)%19==0 and i%100==23:
        for j in range(len(s)):
            maxs = max(maxs,sc(s[j]))
        print(i, maxs)
        k+=1
        maxs = 0
        if k==7:
            break

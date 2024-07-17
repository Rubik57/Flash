maxs = 0
for n in range(0, 50 + 1, 2):
    for m in range(1, 50 + 1, 2):
        A = 5**n + 3**m
        if m%10==5 and n%10!=6 and A%13==0:
            print(n,m)
            maxs = max(maxs, n+m)
print(maxs)

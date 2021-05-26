r,c=[int(v) for v in input().split()]
m=[]
for row in range(r):
    curr=[int(v) for v in input().split()]
    m.append(curr)
for row in range(r-1,-1,-1):
    print(sum(m[row]),end=" ")

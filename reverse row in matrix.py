r,c=[int(v) for v in input().split()]
m=[]
for i in range(r):
    curr=[int(v)+1 for v in input().split()]
    m.append(curr)
for row in range(r-1,-1,-1):
    print(m[row],end=",")

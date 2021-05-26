r=int(input())
m=[]
for i in range(r):
    curr=[int(v) for v in input().split()]
    m.append(curr)
n1,n2=input().split()
n1,n2=int(n1),int(n2)
print(m[n1-1][n2-1])

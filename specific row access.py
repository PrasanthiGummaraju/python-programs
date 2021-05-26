n=int(input())
m=[]
for row in range(n):
    curr=[int(v) for v in input().split()]
    m.append(curr)
row=int(input())
print(*m[row-1])
for i in range(n):
    print(m[i][row-1],end=" ")

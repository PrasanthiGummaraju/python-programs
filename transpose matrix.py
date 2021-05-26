r,c=[int(v) for v in input().split()]
m=[]
for row in range(r):
    curr=[int(v) for v in input().split()]
    m.append(curr)
for col in range(c):
    for row in range(r):
        print(m[row][col],end=" ")
    print()
